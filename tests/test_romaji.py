import codecs

import pytest
from utils import register_codec

from alternative_encodings import romaji


@pytest.fixture(scope="module", autouse=True)
def register_codec_fixture():
    with register_codec(romaji):
        yield


source_data = """
"Go to Combat Training","戦闘訓練へ"
"Organize Combat Training","戦闘訓練を組織する"
"""

encoded = b"""
"Go to Combat Training","Sentou kunren e"
"Organize Combat Training","Sentou kunren wo soshiki suru"
"""


@pytest.mark.parametrize("source_data, encoded",
    [
        (source_data, encoded),
        ("\r\n", b"\r\n"),
        ("吾輩は猫である。 名前はまだ無い。", b"Wagahai wa neko de aru. Namae wa mada nai."),
    ],
)
def test_encode(source_data, encoded):
    assert codecs.encode(source_data, "romaji") == encoded
