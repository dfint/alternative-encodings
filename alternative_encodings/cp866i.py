import codecs
import contextlib
from encodings import cp866


# Codec APIs
class Codec(cp866.Codec):
    def encode(self, input_string: str, errors: str = "strict") -> bytes:
        input_string = input_string.replace("і", "i").replace("І", "I")  # noqa: RUF001
        return super().encode(input_string, errors)


class IncrementalEncoder(cp866.IncrementalEncoder):
    def encode(self, input_string: str, final: bool = False) -> bytes:  # noqa: FBT001, FBT002
        input_string = input_string.replace("і", "i").replace("І", "I")  # noqa: RUF001
        return super().encode(input_string, final)


IncrementalDecoder = cp866.IncrementalDecoder

# encodings module API
codec = Codec()


codec_info = codecs.CodecInfo(
    name="cp866i",
    encode=codec.encode,
    decode=codec.decode,
    incrementalencoder=IncrementalEncoder,
    incrementaldecoder=IncrementalDecoder,
)


def search_function(encoding: str) -> codecs.CodecInfo | None:
    if codec_info.name == encoding:
        return codec_info

    return None


def register() -> None:
    codecs.register(search_function)


def unregister() -> None:
    with contextlib.suppress(AttributeError):
        codecs.unregister(search_function)
