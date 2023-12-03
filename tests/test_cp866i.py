import codecs

import pytest
import alternative_encodings.cp866i as cp866i
from utils import codec


@pytest.fixture(scope="module", autouse=True)
def register_codec():
    with codec(cp866i):
        yield


source_data = "У Іўі худы жвавы чорт у зялёнай камізэльцы пабег пад'есці фаршу з юшкай"
encoded = (
    b"\x93 I\xf7i \xe5\xe3\xa4\xeb \xa6\xa2\xa0\xa2\xeb \xe7\xae\xe0\xe2 \xe3 \xa7\xef\xab\xf1\xad\xa0\xa9 " +
    b"\xaa\xa0\xaci\xa7\xed\xab\xec\xe6\xeb \xaf\xa0\xa1\xa5\xa3 \xaf\xa0\xa4'\xa5\xe1\xe6i \xe4\xa0\xe0\xe8\xe3 " +
    b"\xa7 \xee\xe8\xaa\xa0\xa9"
)


def test_viscii_encode():
    assert codecs.encode(source_data, "cp866i") == encoded


def test_viscii_decode():
    result = codecs.decode(encoded, "cp866i")
    result = result.replace("i", "і").replace("I", "І")
    assert result == source_data
