from typing import Literal,Callable
import io,os,numpy,cv2 as cv

def reverse_bits(byte:int) -> int:
    # b"\x80"(0b1000 0000) to 0x01(0b0000 0001)
    # b"\x01"(0b0000 0001) to 0x80(0b1000 0000)
    reversed_bits = ('0'*(8-len(bin(byte)[2:]))+bin(byte)[2:])[::-1]  # 反转比特位
    return int(reversed_bits, 2)

def reverse_bits_bytes(data:bytes):
    l = list()
    for byte in data:
        l.append(reverse_bits(byte))
    return bytes(l)

class PCF:
    class Table: 
        class toc_entry: # 表的索引
            class field:
                def __init__(self, bytes:bytes) -> None:
                    self.value = int.from_bytes(bytes, "little")
                def __bytes__(self) -> bytes:
                    return self.value.to_bytes(4, "little")
                def __str__(self) -> str:
                    return self.__bytes__().hex()
            class type_field(field):
                types = {
                    (1<<0):"PCF_PROPERTIES",
                    (1<<1):"PCF_ACCELERATORS",
                    (1<<2):"PCF_METRICS",
                    (1<<3):"PCF_BITMAPS",
                    (1<<4):"PCF_INK_METRICS",
                    (1<<5):"PCF_BDF_ENCODINGS",
                    (1<<6):"PCF_SWIDTHS",
                    (1<<7):"PCF_GLYPH_NAMES",
                    (1<<8):"PCF_BDF_ACCELERATORS",
                }
                def __init__(self, bytes: bytes) -> None:
                    super().__init__(bytes)
                    self.type = self.types[self.value]
                def __str__(self) -> str:
                    return self.type
            class format_field(field):
                types = {
                    0x00000000:"PCF_DEFAULT_FORMAT",
                    0x00000200:"PCF_INKBOUNDS",
                    0x00000100:"PCF_ACCEL_W_INKBOUNDS",
                    0x00000100:"PCF_COMPRESSED_METRICS",
                }
                mask = {
                    "PCF_GLYPH_PAD_MASK":(3<<0),
                    "PCF_BYTE_MASK"     :(1<<2),
                    "PCF_BIT_MASK"      :(1<<3),
                    "PCF_SCAN_UNIT_MASK":(3<<4),
                }
                bitModes = {
                    0b00000000          :"Least significant bit first",
                    mask["PCF_BIT_MASK"]:"Most significant bit first",
                }
                byteModes = { 
                    0b00000000           :"little",
                    mask["PCF_BYTE_MASK"]:"big",
                }
                def __init__(self, bytes: bytes) -> None:
                    super().__init__(bytes)
                    self.type = self.types[bytes[1]<<8] if bytes[1]<<8 != 0x00000100 else 0x00000100
                    self.bitMode = self.bitModes[int.from_bytes(bytes, "little") & self.mask["PCF_BIT_MASK"]]
                    self.byteMode = self.byteModes[int.from_bytes(bytes, "little") & self.mask["PCF_BYTE_MASK"]]
                def __str__(self) -> str:
                    return f"{self.type}:{{bitMode:{self.bitMode}, byteMode:{self.byteMode}}}"
            class size_field(field):
                def __new__(cls, bytes: bytes):
                    return int.from_bytes(bytes, "little")
            class offset_field(field):
                def __new__(cls, bytes: bytes):
                    return int.from_bytes(bytes, "little")
            def __init__(self, bytes:bytes) -> None:
                self.type = self.type_field(bytes[0:4])
                self.format = self.format_field(bytes[4:8])
                self.size = self.size_field(bytes[8:12])
                self.offset = self.offset_field(bytes[12:16])
            def __str__(self) -> str:
                return f"{{type: {self.type}, format: {self.format}, size: {self.size}, offset: {hex(self.offset)}}}"
        def __init__(self, file:io.BufferedReader, offset:int) -> None:
            file.seek(offset)
            self.file = file
            self.format = self.toc_entry.format_field(self.file.read(4))
        def read(self, size:int, seek:int=-1, bitMode:Literal['Least significant bit first','Most significant bit first',None]=None) -> bytes: 
            self.file.seek(0 if seek == -1 else seek, os.SEEK_CUR if seek == -1 else os.SEEK_SET)
            data = self.file.read(size)
            if bitMode is None :
                # bitMode = self.format.bitMode
                if self.format.bitMode == "Least significant bit first":
                    return reverse_bits_bytes(data)
                elif self.format.bitMode == "Most significant bit first":
                    return data
            if bitMode == "Least significant bit first":
                return reverse_bits_bytes(data)
            elif bitMode == "Most significant bit first":
                return data
            raise Exception(f"bitMode ERROR")
        def read2int(self, size:int, seek:int=-1, bitMode:Literal['Least significant bit first','Most significant bit first',None]=None, signed: bool = False) -> int: 
            return self.bytes2int(self.read(size, seek, bitMode), signed)
        def bytes2int(self, bytes:bytes, signed: bool = False) -> int:
            return int.from_bytes(bytes, self.format.byteMode, signed=signed)
    class HeaderTable(Table):
        def __init__(self, file:io.BufferedReader) -> None:
            head = file.read(4)
            if head != b"\x01fcp":
                raise Exception(f"this file is not PCF file")
            self.table_count = int.from_bytes(file.read(4), "little")
            self.tables = list()
            for i in range(self.table_count):
                self.tables.append(self.toc_entry(file.read(16)))
        def __str__(self) -> str:
            string = "{\n\r"
            string += f"    table_count: {self.table_count},\n\r"
            string += "    tables: {\n\r"
            for i in self.tables:
                string += f"        {i},\n\r"
            string += "    }\n\r"
            string += "}"
            return string
    class PropertiesTable(Table):
        class prop:
            def __init__(self, bytes:bytes, bytes2int:Callable[[bytes],int]) -> None:
                self.name_offset = bytes2int(bytes[0:4]) # name in string offset
                self.isStringProp = bytes[4] # 0 is value = value,1 is value in string offset
                self.value = bytes2int(bytes[5:9])
            def __repr__(self) -> str:
                return f"{{name_offset:{self.name_offset},isStringProp:{self.isStringProp},value:{self.value}}}"
        def __init__(self, file:io.BufferedReader, offset:int) -> None:
            super().__init__(file, offset)
            self.nprops = self.read2int(4, bitMode="Most significant bit first")
            self.props = list() 
            for i in range(self.nprops):
                self.props.append(self.prop(self.read(9, bitMode="Most significant bit first"),self.bytes2int))
            self.padding = (self.nprops&3)==0 if 0 else (4-(self.nprops&3)) 
            self.read(self.padding)
            self.string_size = self.read2int(4, bitMode="Most significant bit first")
            self.string = self.read(self.string_size, bitMode="Most significant bit first")
        def propsParse(self, props:prop):
            ret = dict()
            def read_string(string:bytes, seek:int) -> str:
                end = seek
                while not string[end] == 0:
                    end += 1
                return string[seek:end].decode()
            if props.isStringProp == 0:
                ret[read_string(self.string, props.name_offset)] = props.value
            else:
                ret[read_string(self.string, props.name_offset)] = read_string(self.string, props.value)
            return ret
        def __str__(self) -> str:
            string = "{\n\r"
            string += f"    nprops: {self.nprops},\n\r"
            string += "    props: {\n\r"
            for props in self.props_l:
                string += f"        {self.propsParse(props)},\n\r"
            string += "    }\n\r"
            string += "}"
            return string
    class MetricsData():
        def __init__(self, bytes:bytes, byteMode, compress:bool=False) -> None:
            if compress:
                self.left_sided_bearing = bytes[0] - 0x80
                self.right_side_bearing = bytes[1] - 0x80
                self.character_width = bytes[2] - 0x80
                self.character_ascent = bytes[3] - 0x80
                self.character_descent = bytes[4] - 0x80
                self.character_attributes = 0
            else:
                self.left_sided_bearing = int.from_bytes(bytes[0:2], byteMode, signed=True)
                self.right_side_bearing = int.from_bytes(bytes[2:4], byteMode, signed=True)
                self.character_width = int.from_bytes(bytes[4:6], byteMode, signed=True)
                self.character_ascent = int.from_bytes(bytes[6:8], byteMode, signed=True)
                self.character_descent = int.from_bytes(bytes[8:10], byteMode, signed=True)
                self.character_attributes = int.from_bytes(bytes[10:12], byteMode)
        def __str__(self):
            string = "{"
            string += f"\n    left_sided_bearing:{self.left_sided_bearing},"
            string += f"\n    right_side_bearing:{self.right_side_bearing},"
            string += f"\n    character_width:{self.character_width},"
            string += f"\n    character_ascent:{self.character_ascent},"
            string += f"\n    character_descent:{self.character_descent},"
            string += f"\n    character_attributes:{self.character_attributes},"
            string += "\n}"
            return string
    class AcceleratorTable(Table):
        def __init__(self, file: io.BufferedReader, offset:int) -> None:
            super().__init__(file, offset)
            self.format.type = "PCF_ACCEL_W_INKBOUNDS" if self.format.type == 0x00000100 else self.format.type
            self.noOverlap = self.read2int(1, bitMode="Most significant bit first")
            self.constantMetrics = self.read2int(1, bitMode="Most significant bit first")
            self.terminalFont = self.read2int(1, bitMode="Most significant bit first")
            self.constantWidth = self.read2int(1, bitMode="Most significant bit first")
            self.inkInside = self.read2int(1, bitMode="Most significant bit first")
            self.inkMetrics = self.read2int(1, bitMode="Most significant bit first")
            self.drawDirection = self.read2int(1, bitMode="Most significant bit first")
            self.padding = self.read2int(1, bitMode="Most significant bit first")
            self.fontAscent = self.read2int(4, bitMode="Most significant bit first", signed=True)
            self.fontDescent = self.read2int(4, bitMode="Most significant bit first", signed=True)
            self.maxOverlap = self.read2int(4, bitMode="Most significant bit first", signed=True)
            self.minbounds = PCF.MetricsData(self.read(12), self.format.byteMode)
            self.maxbounds = PCF.MetricsData(self.read(12), self.format.byteMode)
        def __str__(self):
            string = "{"
            string += f"\n    noOverlap:{self.noOverlap}"
            string += f"\n    constantMetrics:{self.constantMetrics}"
            string += f"\n    terminalFont:{self.terminalFont}"
            string += f"\n    constantWidth:{self.constantWidth}"
            string += f"\n    inkInside:{self.inkInside}"
            string += f"\n    inkMetrics:{self.inkMetrics}"
            string += f"\n    drawDirection:{self.drawDirection}"
            string += f"\n    padding:{self.padding}"
            string += f"\n    fontAscent:{self.fontAscent}"
            string += f"\n    fontDescent:{self.fontDescent}"
            string += f"\n    maxOverlap:{self.maxOverlap}"
            string += f"\n    minbounds:{self.minbounds}"
            string += f"\n    maxbounds:{self.maxbounds}"
            string += "\n}"
            return string
    class MetricsTable(Table):
        def __init__(self, file: io.BufferedReader, offset:int) -> None:
            super().__init__(file, offset)
            self.format.type = "PCF_COMPRESSED_METRICS" if self.format.type == 0x00000100 else self.format.type
            if self.format.type == "PCF_DEFAULT_FORMAT":
                self.metrics_count = self.read2int(4, bitMode="Most significant bit first")
                compress = False
                metricsDataLen = 12
            elif self.format.type == "PCF_COMPRESSED_METRICS":
                self.metrics_count = self.read2int(2, bitMode="Most significant bit first")
                compress = True
                metricsDataLen = 5
            self.metrics = list()
            for _ in range(self.metrics_count):
                self.metrics.append(PCF.MetricsData(self.read(metricsDataLen, bitMode="Most significant bit first"), self.format.byteMode, compress))
    class BitmapTable(Table):
        def __init__(self, file: io.BufferedReader, offset:int) -> None:
            super().__init__(file, offset)
            self.PCF_GLYPH_PAD = {0:1, 1:2, 2:4}[self.format.value&3]
            self.PCF_SCAN_UNIT = {0:1, 1:2, 2:4}[(self.format.value>>4)&3]
            self.glyph_count = self.read2int(4, bitMode="Most significant bit first", signed=True)
            self.offsets = list()
            for _ in range(self.glyph_count):
                self.offsets.append(self.read2int(4, bitMode="Most significant bit first", signed=True))
            self.bitmapSizes = [
                self.read2int(4, bitMode="Most significant bit first", signed=True),
                self.read2int(4, bitMode="Most significant bit first", signed=True),
                self.read2int(4, bitMode="Most significant bit first", signed=True),
                self.read2int(4, bitMode="Most significant bit first", signed=True),
            ]
            self.bitmap_data = self.read(self.bitmapSizes[self.format.value&3], bitMode="Most significant bit first")
    class EncodingTable(Table):
        def __init__(self, file: io.BufferedReader, offset:int) -> None:
            super().__init__(file, offset)
            self.min_char_or_byte2 = self.read2int(2, bitMode="Most significant bit first", signed=True)
            self.max_char_or_byte2 = self.read2int(2, bitMode="Most significant bit first", signed=True)
            self.min_byte1 = self.read2int(2, bitMode="Most significant bit first", signed=True)
            self.max_byte1 = self.read2int(2, bitMode="Most significant bit first", signed=True)
            self.default_char = self.read2int(2, bitMode="Most significant bit first", signed=True)
            self.glyphindeces = list()
            for _ in range((self.max_char_or_byte2-self.min_char_or_byte2+1)*(self.max_byte1-self.min_byte1+1)):
                self.glyphindeces.append(self.read2int(2, bitMode="Most significant bit first"))
    class ScalableWidthsTable(Table):
        def __init__(self, file: io.BufferedReader, offset: int) -> None:
            super().__init__(file, offset)
            self.glyph_count = self.read2int(4, bitMode="Most significant bit first", signed=True)
            self.swidths = list()
            for _ in range(self.glyph_count):
                self.swidths.append(self.read2int(4, bitMode="Most significant bit first", signed=True))
    class GlyphNamesTable(Table):
        def __init__(self, file: io.BufferedReader, offset: int) -> None:
            super().__init__(file, offset)
            self.glyph_count = self.read2int(4, bitMode="Most significant bit first", signed=True)
            self.offsets = list()
            for _ in range(self.glyph_count):
                self.offsets.append(self.read2int(4, bitMode="Most significant bit first", signed=True))
            self.string_size = self.read2int(4, bitMode="Most significant bit first", signed=True)
            self.string = self.read(self.string_size)
    def __init__(self, filePath:str) -> None:
        with open(filePath,"rb") as file:
            self.headTable = self.HeaderTable(file)
            self.propertiesTable = self.PropertiesTable(file, self.headTable.tables[0].offset)
            self.acceleratorTable = self.AcceleratorTable(file, self.headTable.tables[1].offset)
            self.metricsTable = self.MetricsTable(file, self.headTable.tables[2].offset)
            self.bitmapTable = self.BitmapTable(file, self.headTable.tables[3].offset)
            self.encodingTable = self.EncodingTable(file, self.headTable.tables[4].offset)
            self.scalableWidthsTable = self.ScalableWidthsTable(file, self.headTable.tables[5].offset)
            self.glyphNamesTable = self.GlyphNamesTable(file, self.headTable.tables[6].offset)
    def encode(self, char:bytes) -> int:
        # return glyphIndex
        if len(char) == 2:
            return self.encodingTable.glyphindeces[(char[0]-self.encodingTable.min_byte1)*(self.encodingTable.max_char_or_byte2-self.encodingTable.min_char_or_byte2+1)+ char[1]-self.encodingTable.min_char_or_byte2]
        return self.encodingTable.glyphindeces[char[0]-self.encodingTable.min_char_or_byte2]
    def encodeChar(self, char:str) -> int:
        # return glyphIndex
        char = ord(char)
        return self.encode(char.to_bytes(1 if -1<char<256 else 2, "big"))
    def getGlyphWidth(self, glyphIndex:int) -> int:
        return self.metricsTable.metrics[glyphIndex].character_width
    def printGlyph(self, glyphIndex:int, zero:str="0", one:str="1") -> None:
        glyphWidth = self.getGlyphWidth(glyphIndex)
        glyph = self.bitmapTable.bitmap_data[self.bitmapTable.offsets[glyphIndex]:self.bitmapTable.offsets[glyphIndex+1]]
        string = str()
        for i in range(0, len(glyph), self.bitmapTable.PCF_GLYPH_PAD):
            for n in (glyph[i:i+glyphWidth//8]):
                s = ('0'*(8-len(bin(n)[2:]))+bin(n)[2:]).replace("0",zero).replace("1",one)
                string += s if self.bitmapTable.format.bitMode=="Most significant bit first" else s[::-1]
            string += "\n"
        print(string)
    def printGlyphToArray(self,array:numpy.ndarray, arrayStartIndex:int, glyphIndex:int, arrayRowStep:int=0) -> int:
        glyphPaddingLength = self.bitmapTable.PCF_GLYPH_PAD
        glyph = self.bitmapTable.bitmap_data[self.bitmapTable.offsets[glyphIndex]:self.bitmapTable.offsets[glyphIndex+1]]
        glyphWidth = self.getGlyphWidth(glyphIndex)
        arrayIndex = iter(range(arrayStartIndex, arrayStartIndex+16*glyphWidth))
        arrayRowOffset = 0
        for i in range(0, len(glyph), glyphPaddingLength):
            for n,_ in zip(glyph[i:i+glyphPaddingLength], range(glyphWidth//8)):
                byte = '0'*(8-len(bin(n)[2:]))+bin(n)[2:]
                for bit in (byte if self.bitmapTable.format.bitMode=="Most significant bit first" else byte[::-1]):
                    array[next(arrayIndex)+arrayRowOffset] = {"0":0b00000000,"1":0b11111111}[bit]
            arrayRowOffset += arrayRowStep
        return glyphWidth
    def printGlyphToImage(self, imageFilePath:str, glyphIndex:int):
        glyphWidth:int = self.getGlyphWidth(glyphIndex)
        image = numpy.empty(16*glyphWidth,numpy.uint8)
        self.glyphPrintToArray(image, 0, glyphIndex)
        image.shape = (16,glyphWidth)
        cv.imwrite(imageFilePath, image)
    def printStringToImage(self, imageFilePath:str ,string:str):
        imageWidth = 0
        charWidth = dict()
        for char in string: 
            charWidth[char] = self.getGlyphWidth(self.encodeChar(char))
            imageWidth += charWidth[char]
        image = numpy.zeros(16*imageWidth,numpy.uint8)
        imageOffset = 0
        for char in string:
            self.printGlyphToArray(image, imageOffset, self.encodeChar(char), imageWidth-charWidth[char])
            imageOffset += charWidth[char]
        image.shape = (16,imageWidth)
        cv.imwrite(imageFilePath, image)
    def stringRoll(self,string:str, sleepTime:int=1000):
        def cut(shape, source):
            array = numpy.empty(shape, numpy.uint8)
            index = iter(range(shape))
            width = source.shape[1]//3 
            for line in range(source.shape[0]):
                for i in range(source.shape[1]):
                    if width <= i < width*2:
                        array[next(index)] = source[line, i]
            array.shape = (16, source.shape[1]//3)
            return array
        imageWidth = 0
        charWidth = dict()
        for char in string: 
            charWidth[char] = self.getGlyphWidth(self.encodeChar(char))
            imageWidth += charWidth[char]
        while True:
            for n in range(imageWidth*2, 0, -1):
                image = numpy.zeros(16*(imageWidth*3),numpy.uint8)
                imageOffset = n
                for char in string:
                    self.printGlyphToArray(image, imageOffset, self.encodeChar(char), (imageWidth*3)-charWidth[char])
                    imageOffset += charWidth[char]
                image.shape = (16,(imageWidth*3))
                img = cut(16*imageWidth, image)
                #cv.imwrite("./img.bmp", img)
                cv.imshow("image", img)
                cv.waitKey(sleepTime)
