# font-parser
一个用于解析PCF字体文件的Python库

## Use
```Python
from fontparse import PCF
font = PCF("./unifont-15.1.04-l.pcf") # your PCF file
font.printGlyph(font.encodeChar("a"), " ", "*")
```
