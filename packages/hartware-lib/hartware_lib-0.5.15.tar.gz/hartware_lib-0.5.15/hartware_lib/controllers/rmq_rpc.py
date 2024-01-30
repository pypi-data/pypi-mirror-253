from __future__ import annotations

import asyncio
import traceback
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Any, AsyncIterator, Dict, Optional, Union

from hartware_lib.adapters.rabbitmq import (
    RabbitMQAdapter,
    RabbitMQDefaultExchangeAdapter,
)
from hartware_lib.settings import RabbitMQSettings


class RpcProbe:
    def __init__(
        self,
        rpc_in: RabbitMQDefaultExchangeAdapter,
        rpc_out: RabbitMQDefaultExchangeAdapter,
        subject: Any,
    ):
        self.rpc_in = rpc_in
        self.rpc_out = rpc_out
        self.subject = subject

    async def run(self) -> None:
        await self.rpc_in.consume(self.handle_message)  # type: ignore[arg-type]

    async def handle_message(
        self, _origin: RabbitMQDefaultExchangeAdapter, message: Any
    ) -> None:
        assert isinstance(message, dict)

        func = message.get("func")
        property = message.get("property")
        property_set = message.get("property_set")
        args = message.get("args") or []
        kwargs = message.get("kwargs") or {}

        if not func and not property:
            await self.rpc_out.publish(
                {"error": "should have func or property specified"}
            )

            return

        result = None
        try:
            if func:
                func = getattr(self.subject, func)

                if asyncio.iscoroutinefunction(func):
                    result = await func(*args, **kwargs)
                else:
                    result = func(*args, **kwargs)
            else:
                assert isinstance(property, str)

                if "property_set" in message:
                    setattr(self.subject, property, property_set)
                else:
                    result = getattr(self.subject, property)
        except Exception:
            await self.rpc_out.publish({"error": traceback.format_exc()})

            return

        await self.rpc_out.publish({"result": result})


class RpcCaller:
    _none_value = object()
    _max_wait_loop = 150

    def __init__(
        self,
        rpc_in: RabbitMQDefaultExchangeAdapter,
        rpc_out: RabbitMQDefaultExchangeAdapter,
    ):
        self.rpc_in = rpc_in
        self.rpc_out = rpc_out

        self._result: Union[object, Dict[str, Any]] = self._none_value
        self.command_lock = asyncio.Lock()
        self.consumer_task: Optional[asyncio.Task[Any]] = None

    def listen(self) -> None:
        self.consumer_task = asyncio.create_task(self.rpc_out.consume(self._store_result))  # type: ignore[arg-type]

    async def _store_result(
        self, _origin: RabbitMQDefaultExchangeAdapter, result: Dict[str, Any]
    ) -> None:
        self._result = result

    async def get_property(self, name: str) -> Any:
        return await self._process({"property": name})

    async def set_property(self, name: str, value: Any) -> None:
        await self._process({"property": name, "property_set": value})

    async def call(self, func: str, *args: Any, **kwargs: Any) -> Any:
        return await self._process({"func": func, "args": args, "kwargs": kwargs})

    async def _process(self, request: Dict[str, Any]) -> Any:
        self._result = self._none_value

        async with self.command_lock:
            await self.rpc_in.publish(request)

            for _ in range(self._max_wait_loop):
                if self._result != self._none_value:
                    assert isinstance(self._result, dict)

                    error = self._result.get("error")

                    if error:
                        raise Exception(f"{error}")

                    return self._result.get("result")
                await asyncio.sleep(0.2)
            raise Exception("Command Timeout")

    async def stop(self) -> None:
        if self.consumer_task and not self.consumer_task.done():
            self.consumer_task.cancel()

            await asyncio.wait([self.consumer_task])


@dataclass
class RmqRpcController:
    rpc_in: RabbitMQDefaultExchangeAdapter
    rpc_out: RabbitMQDefaultExchangeAdapter

    @classmethod
    def build(
        cls, rabbitmq_settings: RabbitMQSettings, queue_name: str, **kwargs: Any
    ) -> RmqRpcController:
        rabbitmq = RabbitMQAdapter.build(settings=rabbitmq_settings, **kwargs)

        rpc_in = rabbitmq.get_flavor_adapter("default", routing_key=f"{queue_name}_in")
        rpc_out = rabbitmq.get_flavor_adapter(
            "default", routing_key=f"{queue_name}_out"
        )

        assert isinstance(rpc_in, RabbitMQDefaultExchangeAdapter)
        assert isinstance(rpc_out, RabbitMQDefaultExchangeAdapter)

        return cls(rpc_in, rpc_out)

    @asynccontextmanager
    async def connected(self) -> AsyncIterator[None]:
        async with await self.rpc_in.connect():
            async with await self.rpc_out.connect():
                yield

    def get_probe(self, subject: object) -> RpcProbe:
        return RpcProbe(self.rpc_in, self.rpc_out, subject)

    def get_caller(self) -> RpcCaller:
        return RpcCaller(self.rpc_in, self.rpc_out)
