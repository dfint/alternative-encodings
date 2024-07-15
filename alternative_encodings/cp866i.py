import codecs
from encodings import cp866

from alternative_encodings.common import CodecBase


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
_codec = Codec()


class Cp866iCodec(CodecBase):
    codec_info = codecs.CodecInfo(
        name="cp866i",
        encode=_codec.encode,
        decode=_codec.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
    )

    def get_codec_info(self) -> codecs.CodecInfo:
        return self.codec_info


codec = Cp866iCodec()
