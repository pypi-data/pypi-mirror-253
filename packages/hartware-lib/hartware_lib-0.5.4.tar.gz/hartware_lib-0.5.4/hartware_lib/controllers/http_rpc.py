from __future__ import annotations

import asyncio
import traceback
from dataclasses import dataclass
from typing import Any

from aiohttp import ClientSession, web

from hartware_lib.serializers import DeserializerBuilder, SerializerBuilder
from hartware_lib.types import AnyDict, Deserializer, Serializer


@dataclass
class HttpRpcSettings:
    host: str
    port: int
    server_host: str
    server_port: int


@dataclass
class HttpRpcProbe:
    app: web.Application
    subject: Any
    settings: HttpRpcSettings
    serializer: Serializer
    deserializer: Deserializer

    @classmethod
    def build(
        cls,
        settings: HttpRpcSettings,
        subject: Any,
        serializer: Serializer,
        deserializer: Deserializer,
    ) -> HttpRpcProbe:
        app = web.Application()
        obj = cls(app, subject, settings, serializer, deserializer)

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
                status=400,
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
            return web.Response(
                status=400, body=self.serializer({"error": traceback.format_exc()})
            )

        return web.Response(body=self.serializer({"result": result}))

    async def run(self) -> None:
        runner = web.AppRunner(self.app)
        await runner.setup()

        site = web.TCPSite(runner, self.settings.server_host, self.settings.server_port)
        await site.start()


@dataclass
class HttpRpcCaller:
    settings: HttpRpcSettings
    serializer: Serializer
    deserializer: Deserializer

    @classmethod
    def build(
        cls,
        settings: HttpRpcSettings,
        serializer: Serializer,
        deserializer: Deserializer,
    ) -> HttpRpcCaller:
        return cls(settings, serializer, deserializer)

    async def _process(self, data: AnyDict) -> Any:
        session = ClientSession()
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


@dataclass
class HttpRpcController:
    settings: HttpRpcSettings
    serializer: Serializer
    deserializer: Deserializer

    @classmethod
    def build(
        cls,
        http_rpc_settings: HttpRpcSettings,
        serializer: Serializer = SerializerBuilder().get(),
        deserializer: Deserializer = DeserializerBuilder().get(),
    ) -> HttpRpcController:
        return cls(http_rpc_settings, serializer, deserializer)

    def get_probe(self, subject: object) -> HttpRpcProbe:
        return HttpRpcProbe.build(
            self.settings, subject, self.serializer, self.deserializer
        )

    def get_caller(self) -> HttpRpcCaller:
        return HttpRpcCaller.build(self.settings, self.serializer, self.deserializer)
