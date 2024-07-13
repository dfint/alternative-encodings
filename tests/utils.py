import contextlib
from typing import Protocol


class CodecModule(Protocol):
    def register(self): ...

    def unregister(self): ...


@contextlib.contextmanager
def register_codec(codec: CodecModule):
    try:
        codec.register()
        yield
    finally:
        codec.unregister()
