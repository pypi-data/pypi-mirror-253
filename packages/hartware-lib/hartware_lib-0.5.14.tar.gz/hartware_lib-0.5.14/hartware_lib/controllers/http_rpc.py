from __future__ import annotations

import asyncio
import traceback
from dataclasses import dataclass
from typing import Any

from aiohttp import ClientSession, web

from hartware_lib.serializers.builders import DeserializerBuilder, SerializerBuilder
from hartware_lib.settings import HttpRpcSettings
from hartware_lib.types import AnyDict, Deserializer, Serializer


@dataclass
class HttpRpcProbe:
    app: web.Application
    runner: web.AppRunner
    subject: Any
    settings: HttpRpcSettings
    serializer: Serializer
    deserializer: Deserializer

    @classmethod
    def build(
        cls,
        settings: HttpRpcSettings,
        subject: Any,
        serializer: Serializer = SerializerBuilder().get(),
        deserializer: Deserializer = DeserializerBuilder().get(),
    ) -> HttpRpcProbe:
        app = web.Application()
        runner = web.AppRunner(app)

        obj = cls(app, runner, subject, settings, serializer, deserializer)

        app.add_routes([web.post("/", obj.handle)])

        return obj

    async def handle(self, request: web.Request) -> web.Response:
        data = (await request.post())["order"]
        assert isinstance(data, str)

        order = self.deserializer(data)
        assert isinstance(order, dict)

        func = order.get("func")
        property = order.get("property")
        property_set = order.get("property_set")
        args = order.get("args") or []
        kwargs = order.get("kwargs") or {}

        if not func and not property:
            return web.Response(
                body=self.serializer(
                    {"error": "should have func or property specified"}
                ),
            )

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

                if "property_set" in order:
                    setattr(self.subject, property, property_set)
                else:
                    result = getattr(self.subject, property)
        except Exception:
            return web.Response(body=self.serializer({"error": traceback.format_exc()}))

        return web.Response(body=self.serializer({"result": result}))

    async def run(self) -> None:
        await self.runner.setup()

        site = web.TCPSite(self.runner, self.settings.host, self.settings.port)
        await site.start()

        await asyncio.Future()

    async def cleanup(self) -> None:
        await self.runner.cleanup()


@dataclass
class HttpRpcCaller:
    settings: HttpRpcSettings
    serializer: Serializer
    deserializer: Deserializer

    @classmethod
    def build(
        cls,
        settings: HttpRpcSettings,
        serializer: Serializer = SerializerBuilder().get(),
        deserializer: Deserializer = DeserializerBuilder().get(),
    ) -> HttpRpcCaller:
        return cls(settings, serializer, deserializer)

    async def _process(self, data: AnyDict) -> Any:
        async with ClientSession() as session:
            response = await session.post(
                f"http://{self.settings.host}:{self.settings.port}/",
                data={"order": self.serializer(data).decode("utf-8")},
            )

            text = await response.text()

        data = self.deserializer(text)
        error = data.get("error")

        if error:
            raise Exception(f"{error}")

        return data.get("result")

    async def get_property(self, name: str) -> Any:
        return await self._process({"property": name})

    async def set_property(self, name: str, value: Any) -> None:
        await self._process({"property": name, "property_set": value})

    async def call(self, func: str, *args: Any, **kwargs: Any) -> Any:
        return await self._process({"func": func, "args": args, "kwargs": kwargs})
