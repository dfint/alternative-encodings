import codecs
import contextlib
from encodings import cp866


# Codec APIs
class Codec(cp866.Codec):
    def encode(self, input, errors="strict"):
        input = input.replace("і", "i").replace("І", "I")
        return super().encode(input, errors)


class IncrementalEncoder(cp866.IncrementalEncoder):
    def encode(self, input, final=False):
        input = input.replace("і", "i").replace("І", "I")
        return super().encode(input, final)


IncrementalDecoder = cp866.IncrementalDecoder

# encodings module API
codec = Codec()


regentry = codecs.CodecInfo(
    name="cp866i",
    encode=codec.encode,
    decode=codec.decode,
    incrementalencoder=IncrementalEncoder,
    incrementaldecoder=IncrementalDecoder,
)


def search_function(encoding):
    if regentry.name == encoding:
        return regentry

    return None


def register() -> None:
    codecs.register(search_function)


def unregister() -> None:
    with contextlib.suppress(AttributeError):
        codecs.unregister(search_function)
