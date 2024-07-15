import codecs

from .common import (
    CodecBase,
    get_codec,
    get_incremental_decoder,
    get_incremental_encoder,
    get_stream_reader,
    get_stream_writer,
)

# Decoding Table

decoding_table = (
    "\x00\x01Ẳ\x03\x04ẴẪ\x07\x08\t\n\x0b\x0c\r\x0e\x0f"
    "▶◀↕‼¶§▬↨↑↓→←∟↔▲▼"
    " !\"#$%&'()*+,-./"
    "0123456789:;<=>?"
    "@ABCDEFGHIJKLMNO"
    "PQRSTUVWXYZ[\\]^_"
    "`abcdefghijklmno"
    "pqrstuvwxyz{|}~\x7f"
    "ÇüéâäàåçêëèïîìÄÅ"
    "ÉæÆôöòûùÿÖÜø£Ø×ƒ"  # noqa: RUF001
    "áíóúñÑªº¿®¬œŒ¡«»"
    "░▒▓│┤ÁÂÀ©╣║╗╝¢¥┐"
    "└┴┬├─┼ãÃ╚╔╩╦╠═╬¤"
    "ðÐÊËÈ€ÍÎÏ┘┌█▄ŠÌ▀"
    "ÓßÔÒõÕµþÞÚÛÙýÝ¯Ž"
    "\xad±\xf2Ÿ¶§÷ž°š·¹³²■\xa0"
)

# Encoding table
encoding_table = codecs.charmap_build(decoding_table)

# Codec APIs
Codec = get_codec(encoding_table=encoding_table, decoding_table=decoding_table)

IncrementalEncoder = get_incremental_encoder(encoding_table=encoding_table)

IncrementalDecoder = get_incremental_decoder(decoding_table=decoding_table)

StreamWriter = get_stream_writer(Codec)

StreamReader = get_stream_reader(Codec)

# encodings module API

_codec = Codec()


class Cp859Codec(CodecBase):
    codec_info = codecs.CodecInfo(
        name="cp859",
        encode=_codec.encode,
        decode=_codec.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
    )

    def get_codec_info(self) -> codecs.CodecInfo:
        return self.codec_info


codec = Cp859Codec()
