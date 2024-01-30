import json
import grpc

from datetime import datetime

from kilmlogger.services.scribe.grpc.scribelog_pb2_grpc import ScribeLogServiceStub
from kilmlogger.services.scribe.grpc.scribelog_pb2 import (
    ListOfEntryRequest,
    LogEntryRequest,
    LogEntry,
)

from kilmlogger.envs import envs


class ScribeBaseClient(object):
    def __init__(
        self,
        host: str | None = envs.SCRIBE_HOST,
        port: str | None = envs.SCRIBE_PORT,
        category: str | None = envs.DP_CATEGORY,
        app_name: str | None = envs.APP_NAME,
        app_prop: str | None = envs.ENVIRONMENT,
        dp_cate: str | None = envs.DP_CATEGORY,
    ):
        self.host = host
        self.port = port
        self.category = category
        self.app_name = app_name
        self.app_prop = app_prop
        self.dp_cate = dp_cate

    @staticmethod
    def build_grpc_stub(host: str, port: str) -> ScribeLogServiceStub:
        channel: grpc.Channel = grpc.insecure_channel(
            target=f"{host}:{port}",
            compression=grpc.Compression.Gzip,
        )
        return ScribeLogServiceStub(channel)

    @property
    def grpc_stub(self) -> ScribeLogServiceStub:
        if not hasattr(self, "_grpc_stub"):
            self._grpc_stub = self.build_grpc_stub(self.host, self.port)
        return self._grpc_stub

    def log(self, msg: dict):
        self.grpc_stub.sendMultiLogV2(
            self._build_request(
                json_param=self._build_dp_params(msg),
            )
        )


class DefaultScribeClient(ScribeBaseClient):
    def _build_request(
        self,
        dp_log: str | None = envs.DP_LOG,
        json_param: dict = {},
    ) -> ListOfEntryRequest:
        return ListOfEntryRequest(
            logEntryRequest=[
                LogEntryRequest(
                    category=self.category,
                    app_name=self.app_name,
                    app_prop=self.app_prop,
                    timestamp=int(datetime.utcnow().timestamp() * 1000),
                    log_entry=LogEntry(
                        json_param=json.dumps(json_param),
                        dp_log=dp_log,
                        dp_cate=self.dp_cate,
                    ),
                )
            ]
        )

    def _build_dp_params(self, msg: dict) -> dict:
        return {
            "log_time": msg["time"],
            "app_name": self.app_name,
            "app_mode": self.app_prop,
            "event_category": msg["level"],
            "correlation_id": msg["correlation_id"],
            "message": {
                "time": msg["time"],
                "content": msg["msg"],
            },
            "metrics": msg.get("metrics", {}),
            "extra_data": msg.get("extra_data", {}),
        }
