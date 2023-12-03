import codecs


def get_codec(encoding_table, decoding_table):
    class Codec(codecs.Codec):
        def encode(self, input, errors="strict"):
            return codecs.charmap_encode(input, errors, encoding_table)

        def decode(self, input, errors="strict"):
            return codecs.charmap_decode(input, errors, decoding_table)
    
    return Codec


def get_incremental_encoder(encoding_table):
    class IncrementalEncoder(codecs.IncrementalEncoder):
        def encode(self, input, final=False):
            return codecs.charmap_encode(input, self.errors, encoding_table)[0]
    
    return IncrementalEncoder


def get_incremental_decoder(decoding_table):
    class IncrementalDecoder(codecs.IncrementalDecoder):
        def decode(self, input, final=False):
            return codecs.charmap_decode(input, self.errors, decoding_table)[0]
    
    return IncrementalDecoder


def get_stream_writer(codec):
    class StreamWriter(codec, codecs.StreamWriter):
        pass
    
    return StreamWriter


def get_stream_reader(codec):
    class StreamReader(codec, codecs.StreamReader):
        pass

    return StreamReader
