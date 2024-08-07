import codecs

import pytest

from alternative_encodings import cp859, cp866i, romaji, viscii

from .utils import register_codec

codecs_pairs = [
    ("cp859", cp859.codec),
    ("cp866i", cp866i.codec),
    ("romaji", romaji.codec),
    ("viscii", viscii.codec),
]


@pytest.mark.parametrize(
    "string",
    [
        "\r\n",
    ],
)
def test_general(string: str):
    for codec_name, codec in codecs_pairs:
        with register_codec(codec):
            encoded = codecs.encode(string, encoding=codec_name)
            decoded = codecs.decode(encoded, encoding=codec_name)
            assert decoded == string
