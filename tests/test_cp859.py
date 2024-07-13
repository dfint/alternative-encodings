import codecs
from collections.abc import Generator

import pytest

from alternative_encodings.cp859 import codec

from .utils import register_codec


@pytest.fixture(scope="module", autouse=True)
def _register_codec_fixture() -> Generator[None, None, None]:
    with register_codec(codec):
        yield


source_data = (
    "J'aime l'idée que le plus grand des Sex-symbols new-yorkais, "
    "n'était qu'un chien dans un foyer de Brazzaville"
)

encoded = (
    b"J'aime l'id\x82e que le plus grand des Sex-symbols "
    b"new-yorkais, n'\x82tait qu'un chien dans un foyer d"
    b"e Brazzaville"
)


@pytest.mark.parametrize(("source_data", "encoded"),
    [
        (source_data, encoded),
        ("\r\n", b"\r\n"),
    ],
)
def test_encode(source_data: str, encoded: bytes):
    assert codecs.encode(source_data, "cp859") == encoded
    assert codecs.decode(encoded, "cp859") == source_data
