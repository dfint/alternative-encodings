import codecs
from collections.abc import Generator

import pytest

from alternative_encodings import viscii

from .utils import register_codec


@pytest.fixture(scope="module", autouse=True)
def _register_codec_fixture() -> Generator[None, None, None]:
    with register_codec(viscii.codec):
        yield


source_data = (
    "ẠẮẰẶẤẦẨẬẼẸẾỀỂỄỆỐ"
    "ỒỔỖỘỢỚỜỞỊỎỌỈỦŨỤỲ"
    "Õắằặấầẩậẽẹếềểễệố"
    "ồổỗỠƠộờởịỰỨỪỬơớƯ"
    "ÀÁÂÃẢĂẳẵÈÉÊẺÌÍĨỳ"
    "ĐứÒÓÔạỷừửÙÚỹỵÝỡư"
    "àáâãảăữẫèéêẻìíĩỉ"
    "đựòóôõỏọụùúũủýợỮ"
    "ẲẴẪỶỸỴ"
)


encoded = bytes(range(0x80, 0x100)) + b"\x02\x05\x06\x14\x19\x1e"


def test_encode():
    assert codecs.encode(source_data, "viscii") == encoded


def test_decode():
    assert codecs.decode(encoded, "viscii") == source_data
