import codecs

import pytest
from utils import register_codec

import alternative_encodings.cp859 as cp859


@pytest.fixture(scope="module", autouse=True)
def register_codec_fixture():
    with register_codec(cp859):
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


def test_encode():
    assert codecs.encode(source_data, "cp859") == encoded
    assert codecs.decode(encoded, "cp859") == source_data
