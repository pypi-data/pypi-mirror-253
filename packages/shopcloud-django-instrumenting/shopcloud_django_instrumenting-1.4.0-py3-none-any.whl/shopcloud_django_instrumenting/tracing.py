import decimal
import itertools
import json
import logging
import os
import time
import traceback
import uuid
from contextlib import contextmanager
from typing import Optional


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super().default(o)


class Base:
    @contextmanager
    def start_span(self, operation: str, **kwargs) -> "Span":
        s = Span(self, operation)
        self.spans.append(s)
        try:
            s.start_at_timestamp = time.process_time()
            yield s
            s.end_at_timestamp = time.process_time()
        except Exception as e:
            s.error = True
            s.exception = e
            s.exception = {
                "code": str(e),
                "traceback": traceback.format_exc().split("\n"),
            }
            s.end_at_timestamp = time.process_time()


class Span(Base):
    def __init__(self, tr: "Tracer", operation: str):
        self.tr = tr
        self.operation = operation
        self.spans = []
        self.tags = {}
        self.logs = []
        self.exception = None
        self.error = False
        # timing
        self.start_at_timestamp = None
        self.end_at_timestamp = None

    def set_tag(self, key: str, value: str):
        self.tags[key] = value

    def log_kv(self, data: dict):
        self.logs.append(data)

    @property
    def tracer_id(self) -> str:
        if isinstance(self.tr, Tracer):
            return self.tr.id
        return self.tr.tracer_id

    def get_spans(self):
        return [self] + [y for x in self.spans for y in x.get_spans()]

    def to_dict(self) -> dict:
        if None not in [
            self.start_at_timestamp,
            self.end_at_timestamp,
        ]:
            run_total = "{:.2f} ms".format(
                (self.end_at_timestamp - self.start_at_timestamp) * 1000.0,
            )
        else:
            run_total = None

        d = {
            "operation": self.operation,
            "run_total": run_total,
        }
        if len(self.tags.values()) > 0:
            d = {
                **d,
                "tags": self.tags,
            }
        if self.exception is not None:
            d = {
                **d,
                "exception": self.exception,
            }
        if len(self.logs) > 0:
            d = {
                **d,
                "logs": self.logs,
            }
        if len(self.spans) > 0:
            d = {
                **d,
                "spans": [x.to_dict() for x in self.spans],
            }
        return d


class Tracer(Base):
    def __init__(self, service: str, operation: str, **kwargs):
        self.id = str(uuid.uuid4())
        self.service = service
        self.operation = operation
        self.spans = []
        self.env = kwargs.get("env", os.environ.get("ENV"))

    @property
    def tracer_id(self) -> str:
        return self.id

    @property
    def is_success(self):
        spans = list(itertools.chain.from_iterable([x.get_spans() for x in self.spans]))
        span_errors = [x.error for x in spans]
        return True not in span_errors

    def serilizer_data(self, data: dict, **kwargs) -> Optional[str]:
        data_serilized = None
        try:
            data_serilized = json.dumps(data, cls=DecimalEncoder)
        except Exception as e:
            if self.env != "production":
                raise e
        return data_serilized

    def close(self, **kwargs) -> dict:
        data = {
            "id": self.id,
            "service": self.service,
            "operation": self.operation,
            "is_success": self.is_success,
            "spans": [x.to_dict() for x in self.spans],
        }

        if kwargs.get("log", True):
            data_serilized = self.serilizer_data(data)
            if data_serilized is not None:
                logging.info(f"instrumenting-trace {data_serilized}")
            else:
                logging.error("instrumenting-error-trace error by convert")

        return data


class DjangoTracer(Tracer):
    def __init__(self, request, **kwargs):
        operation = kwargs.get(
            "operation",
            "HTTP {} {}".format(
                request.method,
                request.path,
            ),
        )
        super().__init__("frontend", operation)
        self.env = kwargs.get("env", os.environ.get("ENV"))
        self.request = request

        if not hasattr(request, "user"):
            user_id = None
        else:
            user = request.user
            if hasattr(user, "id"):
                user_id = user.id
            else:
                if self.env == "production":
                    user_id = None
                else:
                    user_id = user

        self.context = {
            "request": {
                "headers": {
                    "Debug-ID": request.headers.get("Debug-ID"),
                    "User-Agent": request.META.get("HTTP_USER_AGENT"),
                    "X-Appengine-User-Ip": request.headers.get("X-Appengine-User-Ip"),
                    "X-Forwarded-For": request.headers.get("X-Forwarded-For"),
                    "django-user-id": user_id,
                },
                "data": self._request_data(request),
            },
        }

    def _request_data(self, request) -> Optional[dict]:
        return {}

    def close(self, **kwargs) -> dict:
        data = {
            **super().close(log=False),
            "context": self.context,
        }

        if kwargs.get("log", True):
            data_serilized = self.serilizer_data(data, env=kwargs.get("env"))
            if data_serilized is not None:
                logging.info(f"instrumenting-trace {data_serilized}")
            else:
                logging.error("instrumenting-error-trace error by convert")

        return data


class DjangoAPITracer(DjangoTracer):
    def _request_data(self, request) -> Optional[dict]:
        try:
            json.dumps(request.data, cls=DecimalEncoder)
            return request.data
        except Exception as e:
            if self.env != "production":
                raise e
            return {}


class DjangoViewTracer(DjangoTracer):
    def _request_data(self, request) -> Optional[dict]:
        try:
            request_data = {
                "GET": request.GET if hasattr(request, "GET") else None,
                "POST": request.POST if hasattr(request, "POST") else None,
            }
            json.dumps(request_data, cls=DecimalEncoder)
            return request_data
        except Exception as e:
            if self.env != "production":
                raise e
            return {}
