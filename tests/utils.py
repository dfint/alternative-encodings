import contextlib
from typing import Protocol


class CodecModule(Protocol):
    def register(): ...
    def unregister(): ...


@contextlib.contextmanager
def codec(codec: CodecModule):
    try:
        codec.register()
        yield
    finally:
        codec.unregister()
