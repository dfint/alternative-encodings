import codecs
import re
from collections.abc import Iterator
from encodings import cp437

import cutlet

from alternative_encodings.common import CodecBase

katsu = cutlet.Cutlet(use_foreign_spelling=False)


def is_translatable(s: str) -> bool:
    return katsu.romaji(s).strip() != s.strip()


def translate_with_spaces(s: str) -> Iterator[str]:
    start, middle, end = re.search(r"^(\s*)(.*?)(\s*)$", s).groups()
    yield start
    yield katsu.romaji(middle)
    yield end


def iter_translate(input_string: str) -> Iterator[str]:
    for line_with_ending in input_string.splitlines(keepends=True):
        line, end = re.search(r"^(.*?)([\r\n]*)$", line_with_ending, flags=re.MULTILINE + re.DOTALL).groups()
        if line:
            parts = re.split(r"(\b[\w \,]+\b)", line)
            for part in parts:
                yield from translate_with_spaces(part)

        yield end


def encode(input_string: str) -> str:
    return "".join(iter_translate(input_string))


class Codec(cp437.Codec):
    def encode(self, input_string: str, errors: str = "strict") -> bytes:
        return super().encode(encode(input_string), errors)


class IncrementalEncoder(cp437.IncrementalEncoder):
    def encode(self, input_string: str, final: bool = False) -> bytes:  # noqa: FBT001, FBT002
        return super().encode(encode(input_string), final)


IncrementalDecoder = cp437.IncrementalDecoder

# encodings module API
_codec = Codec()


class RomajiCodec(CodecBase):
    codec_info = codecs.CodecInfo(
        name="romaji",
        encode=_codec.encode,
        decode=_codec.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
    )

    def get_codec_info(self) -> codecs.CodecInfo:
        return self.codec_info


codec = RomajiCodec()
