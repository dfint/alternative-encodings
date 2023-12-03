import codecs
import encodings.cp866 as cp866


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


def register():
    codecs.register(search_function)


def unregister():
    try:
        codecs.unregister(search_function)
    except AttributeError:
        pass
