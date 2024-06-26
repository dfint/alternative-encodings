import codecs

import pytest
from utils import register_codec

from alternative_encodings import cp859, cp866i, viscii

codecs_pairs = [
    ("cp859", cp859),
    ("cp866i", cp866i),
    ("viscii", viscii),
]


@pytest.mark.parametrize("string",
    [
        "\r\n",
    ]
)
def test_general(string):
    for codec_name, codec in codecs_pairs:
        with register_codec(codec):
            encoded = codecs.encode(string, encoding=codec_name)
            decoded = codecs.decode(encoded, encoding=codec_name)
            assert decoded == string
