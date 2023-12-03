import codecs

import pytest
import alternative_encodings.viscii as viscii
from utils import codec


@pytest.fixture(scope="module", autouse=True)
def register_codec():
    with codec(viscii):
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


def test_viscii_encode():
    assert codecs.encode(source_data, "viscii") == encoded


def test_viscii_decode():
    assert codecs.decode(encoded, "viscii") == source_data
