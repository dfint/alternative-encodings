import codecs
import contextlib
import re
from collections.abc import Iterator
from encodings import cp437

import cutlet

katsu = cutlet.Cutlet(use_foreign_spelling=False)


def is_translatable(s: str):
    return katsu.romaji(s).strip() != s.strip()


def translate_with_spaces(s: str) -> Iterator[str]:
    start, middle, end = re.search(r"^(\s*)(.*?)(\s*)$", s).groups()
    yield start
    yield katsu.romaji(middle)
    yield end


def iter_translate(input: str) -> Iterator[str]:
    for line_with_ending in input.splitlines(keepends=True):
        line, end = re.search(r"^(.*?)([\r\n]*)$", line_with_ending, flags=re.MULTILINE + re.DOTALL).groups()
        if line:
            parts = re.split(r"(\b[\w \,]+\b)", line)
            for part in parts:
                yield from translate_with_spaces(part)

        yield end


def encode(input: str) -> str:
    return "".join(iter_translate(input))


class Codec(cp437.Codec):
    def encode(self, input, errors="strict"):
        return super().encode(encode(input), errors)


class IncrementalEncoder(cp437.IncrementalEncoder):
    def encode(self, input, final=False):
        return super().encode(encode(input), final)


IncrementalDecoder = cp437.IncrementalDecoder

# encodings module API
codec = Codec()

regentry = codecs.CodecInfo(
    name="romaji",
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
