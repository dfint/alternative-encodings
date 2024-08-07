import codecs
import contextlib
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from _codecs import _EncodingMap


def get_codec(encoding_table: Union[dict[int, int], "_EncodingMap"], decoding_table: str) -> type[codecs.Codec]:
    class Codec(codecs.Codec):
        def encode(self, input_string: str, errors: str = "strict") -> tuple[bytes, int]:
            return codecs.charmap_encode(input_string, errors, encoding_table)

        def decode(self, input_bytes: bytes, errors: str = "strict") -> tuple[str, int]:
            return codecs.charmap_decode(input_bytes, errors, decoding_table)

    return Codec


def get_incremental_encoder(encoding_table: Union[dict[int, int], "_EncodingMap"]) -> type[codecs.IncrementalEncoder]:
    class IncrementalEncoder(codecs.IncrementalEncoder):
        def encode(self, input_string: str, _final: bool = False) -> bytes:  # noqa: FBT001, FBT002
            return codecs.charmap_encode(input_string, self.errors, encoding_table)[0]

    return IncrementalEncoder


def get_incremental_decoder(decoding_table: str) -> type[codecs.IncrementalDecoder]:
    class IncrementalDecoder(codecs.IncrementalDecoder):
        def decode(self, input_bytes: bytes, _final: bool = False) -> str:  # noqa: FBT001, FBT002
            return codecs.charmap_decode(input_bytes, self.errors, decoding_table)[0]

    return IncrementalDecoder


def get_stream_writer(codec: type[codecs.Codec]) -> type[codecs.Codec, codecs.StreamWriter]:
    class StreamWriter(codec, codecs.StreamWriter):
        pass

    return StreamWriter


def get_stream_reader(codec: type[codecs.Codec]) -> type[codecs.Codec, codecs.StreamReader]:
    class StreamReader(codec, codecs.StreamReader):
        pass

    return StreamReader


class CodecBase(ABC):
    @abstractmethod
    def get_codec_info(self) -> codecs.CodecInfo:
        raise NotImplementedError

    def search_function(self, encoding: str) -> codecs.CodecInfo | None:
        codec_info = self.get_codec_info()
        if codec_info.name == encoding:
            return codec_info

        return None

    def register(self) -> None:
        codecs.register(self.search_function)

    def unregister(self) -> None:
        with contextlib.suppress(AttributeError):
            codecs.unregister(self.search_function)
