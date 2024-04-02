import codecs

from .common import get_codec, get_incremental_decoder, get_incremental_encoder, get_stream_reader, get_stream_writer

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
    "ÉæÆôöòûùÿÖÜø£Ø×ƒ"
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

codec = Codec()


regentry = codecs.CodecInfo(
    name="cp859",
    encode=codec.encode,
    decode=codec.decode,
    incrementalencoder=IncrementalEncoder,
    incrementaldecoder=IncrementalDecoder,
)


def search_function(encoding):
    if regentry.name == encoding:
        return regentry

    return None


def register():
    codecs.register(search_function)


def unregister():
    try:
        codecs.unregister(search_function)
    except AttributeError:
        pass
