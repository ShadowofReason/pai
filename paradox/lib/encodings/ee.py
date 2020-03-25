import codecs


class Codec(codecs.Codec):
    def encode(self, input, errors="strict"):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors="strict"):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(
        name="paradox-ee",
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Table

### Decoding Table

decoding_table = (
    "\x00"  #  0x00 -> NULL
    "\x01"  #  0x01 -> START OF HEADING
    "\x02"  #  0x02 -> START OF TEXT
    "\x03"  #  0x03 -> END OF TEXT
    "\x04"  #  0x04 -> END OF TRANSMISSION
    "\x05"  #  0x05 -> ENQUIRY
    "\x06"  #  0x06 -> ACKNOWLEDGE
    "\x07"  #  0x07 -> BELL
    "\x08"  #  0x08 -> BACKSPACE
    "\t"  #  0x09 -> HORIZONTAL TABULATION
    "\n"  #  0x0A -> LINE FEED
    "\x0b"  #  0x0B -> VERTICAL TABULATION
    "\x0c"  #  0x0C -> FORM FEED
    "\r"  #  0x0D -> CARRIAGE RETURN
    "\x0e"  #  0x0E -> SHIFT OUT
    "\x0f"  #  0x0F -> SHIFT IN
    "\x10"  #  0x10 -> DATA LINK ESCAPE
    "\x11"  #  0x11 -> DEVICE CONTROL ONE
    "\x12"  #  0x12 -> DEVICE CONTROL TWO
    "\x13"  #  0x13 -> DEVICE CONTROL THREE
    "\x14"  #  0x14 -> DEVICE CONTROL FOUR
    "\x15"  #  0x15 -> NEGATIVE ACKNOWLEDGE
    "\x16"  #  0x16 -> SYNCHRONOUS IDLE
    "\x17"  #  0x17 -> END OF TRANSMISSION BLOCK
    "\x18"  #  0x18 -> CANCEL
    "\x19"  #  0x19 -> END OF MEDIUM
    "\x1a"  #  0x1A -> SUBSTITUTE
    "\x1b"  #  0x1B -> ESCAPE
    "\x1c"  #  0x1C -> FILE SEPARATOR
    "\x1d"  #  0x1D -> GROUP SEPARATOR
    "\x1e"  #  0x1E -> RECORD SEPARATOR
    "\x1f"  #  0x1F -> UNIT SEPARATOR
    " "  #  0x20 -> SPACE
    "!"  #  0x21 -> EXCLAMATION MARK
    '"'  #  0x22 -> QUOTATION MARK
    "#"  #  0x23 -> NUMBER SIGN
    "$"  #  0x24 -> DOLLAR SIGN
    "%"  #  0x25 -> PERCENT SIGN
    "&"  #  0x26 -> AMPERSAND
    "'"  #  0x27 -> APOSTROPHE
    "("  #  0x28 -> LEFT PARENTHESIS
    ")"  #  0x29 -> RIGHT PARENTHESIS
    "*"  #  0x2A -> ASTERISK
    "+"  #  0x2B -> PLUS SIGN
    ","  #  0x2C -> COMMA
    "-"  #  0x2D -> HYPHEN-MINUS
    "."  #  0x2E -> FULL STOP
    "/"  #  0x2F -> SOLIDUS
    "0"  #  0x30 -> DIGIT ZERO
    "1"  #  0x31 -> DIGIT ONE
    "2"  #  0x32 -> DIGIT TWO
    "3"  #  0x33 -> DIGIT THREE
    "4"  #  0x34 -> DIGIT FOUR
    "5"  #  0x35 -> DIGIT FIVE
    "6"  #  0x36 -> DIGIT SIX
    "7"  #  0x37 -> DIGIT SEVEN
    "8"  #  0x38 -> DIGIT EIGHT
    "9"  #  0x39 -> DIGIT NINE
    ":"  #  0x3A -> COLON
    ";"  #  0x3B -> SEMICOLON
    "<"  #  0x3C -> LESS-THAN SIGN
    "="  #  0x3D -> EQUALS SIGN
    ">"  #  0x3E -> GREATER-THAN SIGN
    "?"  #  0x3F -> QUESTION MARK
    "@"  #  0x40 -> COMMERCIAL AT
    "A"  #  0x41 -> LATIN CAPITAL LETTER A
    "B"  #  0x42 -> LATIN CAPITAL LETTER B
    "C"  #  0x43 -> LATIN CAPITAL LETTER C
    "D"  #  0x44 -> LATIN CAPITAL LETTER D
    "E"  #  0x45 -> LATIN CAPITAL LETTER E
    "F"  #  0x46 -> LATIN CAPITAL LETTER F
    "G"  #  0x47 -> LATIN CAPITAL LETTER G
    "H"  #  0x48 -> LATIN CAPITAL LETTER H
    "I"  #  0x49 -> LATIN CAPITAL LETTER I
    "J"  #  0x4A -> LATIN CAPITAL LETTER J
    "K"  #  0x4B -> LATIN CAPITAL LETTER K
    "L"  #  0x4C -> LATIN CAPITAL LETTER L
    "M"  #  0x4D -> LATIN CAPITAL LETTER M
    "N"  #  0x4E -> LATIN CAPITAL LETTER N
    "O"  #  0x4F -> LATIN CAPITAL LETTER O
    "P"  #  0x50 -> LATIN CAPITAL LETTER P
    "Q"  #  0x51 -> LATIN CAPITAL LETTER Q
    "R"  #  0x52 -> LATIN CAPITAL LETTER R
    "S"  #  0x53 -> LATIN CAPITAL LETTER S
    "T"  #  0x54 -> LATIN CAPITAL LETTER T
    "U"  #  0x55 -> LATIN CAPITAL LETTER U
    "V"  #  0x56 -> LATIN CAPITAL LETTER V
    "W"  #  0x57 -> LATIN CAPITAL LETTER W
    "X"  #  0x58 -> LATIN CAPITAL LETTER X
    "Y"  #  0x59 -> LATIN CAPITAL LETTER Y
    "Z"  #  0x5A -> LATIN CAPITAL LETTER Z
    "["  #  0x5B -> LEFT SQUARE BRACKET
    "¥"  #  0x5C -> YEN
    "]"  #  0x5D -> RIGHT SQUARE BRACKET
    "^"  #  0x5E -> CIRCUMFLEX ACCENT
    "_"  #  0x5F -> LOW LINE
    "`"  #  0x60 -> GRAVE ACCENT
    "a"  #  0x61 -> LATIN SMALL LETTER A
    "b"  #  0x62 -> LATIN SMALL LETTER B
    "c"  #  0x63 -> LATIN SMALL LETTER C
    "d"  #  0x64 -> LATIN SMALL LETTER D
    "e"  #  0x65 -> LATIN SMALL LETTER E
    "f"  #  0x66 -> LATIN SMALL LETTER F
    "g"  #  0x67 -> LATIN SMALL LETTER G
    "h"  #  0x68 -> LATIN SMALL LETTER H
    "i"  #  0x69 -> LATIN SMALL LETTER I
    "j"  #  0x6A -> LATIN SMALL LETTER J
    "k"  #  0x6B -> LATIN SMALL LETTER K
    "l"  #  0x6C -> LATIN SMALL LETTER L
    "m"  #  0x6D -> LATIN SMALL LETTER M
    "n"  #  0x6E -> LATIN SMALL LETTER N
    "o"  #  0x6F -> LATIN SMALL LETTER O
    "p"  #  0x70 -> LATIN SMALL LETTER P
    "q"  #  0x71 -> LATIN SMALL LETTER Q
    "r"  #  0x72 -> LATIN SMALL LETTER R
    "s"  #  0x73 -> LATIN SMALL LETTER S
    "t"  #  0x74 -> LATIN SMALL LETTER T
    "u"  #  0x75 -> LATIN SMALL LETTER U
    "v"  #  0x76 -> LATIN SMALL LETTER V
    "w"  #  0x77 -> LATIN SMALL LETTER W
    "x"  #  0x78 -> LATIN SMALL LETTER X
    "y"  #  0x79 -> LATIN SMALL LETTER Y
    "z"  #  0x7A -> LATIN SMALL LETTER Z
    "{"  #  0x7B -> LEFT CURLY BRACKET
    "|"  #  0x7C -> VERTICAL LINE
    "}"  #  0x7D -> RIGHT CURLY BRACKET
    "Ä"  #  0x84 -> LATIN CAPITAL LETTER A WITH DIAERESIS
    "ä"  #  0xA4 -> LATIN SMALL LETTER A WITH DIAERESIS
    "Õ"  #  0x95 -> LATIN CAPITAL LETTER O WITH TILDE
    "Ö"  #  0x96 -> LATIN CAPITAL LETTER O WITH DIAERESIS
    "Ü"  #  0x9C -> LATIN CAPITAL LETTER U WITH DIAERESIS
    "õ"  #  0xB5 -> LATIN SMALL LETTER O WITH TILDE
    "ö"  #  0xB6 -> LATIN SMALL LETTER O WITH DIAERESIS
    "ü"  #  0xBC -> LATIN SMALL LETTER U WITH DIAERESIS

)

encoding_table = codecs.charmap_build(decoding_table)
