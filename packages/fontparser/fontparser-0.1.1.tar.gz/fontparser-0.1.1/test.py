import src.fontparse as fontparse

font = fontparse.PCF("./unifont-15.1.04-l.pcf")
s = input("请输入写入的文本: ")
#speed = int(input("请输入速度单位ms: "))
font.printGlyph(font.encodeChar(s[0]), " ", "*")