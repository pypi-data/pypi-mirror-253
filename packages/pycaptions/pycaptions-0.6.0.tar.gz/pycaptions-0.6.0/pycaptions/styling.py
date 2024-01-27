import cssutils
import webcolors
import colorsys
import re

from bs4 import BeautifulSoup as BS
from cssutils import CSSParser
from cssutils.css import CSSStyleSheet as originalCSSStyleSheet


class StyleSheet(originalCSSStyleSheet):
    def __json__(self):
        return str(self.cssText)


cssutils.css.CSSStyleSheet = StyleSheet
cssParser = CSSParser(validate=False)

def to_hex2(value):
    return '{:02X}'.format(value)

def get_hexrgb(color):
    if color.startswith("#"):
        if len(color) == 5:
            color = color[:-1]
        if len(color) == 9:
            color = color[:-2]
        return [to_hex2(i) for i in webcolors.hex_to_rgb(color)]
    elif color.endswith(")"):
        if color.startswith("rgb"):
            return [to_hex2(int(i)) for i in color[4:-1].split(",")]
        colors = [re.sub(r'[^0-9.]', '', i)  for i in color[:-1].split("(")[1].split(",")]
        if color.startswith("hsl"):
            h = float(colors[0]) 
            s = float(colors[1])
            l = float(colors[2])
            if h > 1:
                h /= 360
            if s > 1:
                s /= 100
            if l > 1:
                l /= 100
            return [to_hex2(min(int(i*255),255)) for i in colorsys.hls_to_rgb(h,l,s)]
        print(f"No color parser for {color}")
        return ["00","00","00"]
    else:
        return [to_hex2(i) for i in webcolors.name_to_rgb(color)]


class Styling(BS):

    def parseStyle(self, string):
        return cssParser.parseStyle(string, encoding="UTF-8")
    
    def get_lines(self):
        return (BS(line, 'html.parser').get_text() for index, line in enumerate(str(self).split("<br/>")))

    @staticmethod
    def fromSRT(text):
        bs = BS(text, "html.parser")
        if bs.font:
            for tag in bs.find_all("font"):
                tag.name = "span"
                if "color" in tag.attrs:
                    tag["style"] = f'color: {tag["color"]};'
                    del tag["color"]
                if "size" in tag.attrs:
                    tag["style"] = tag.get("style", "")+f'font-size: {tag["size"]}pt;'
                    del tag["size"]
                if "face" in tag.attrs:
                    tag["style"] = tag.get("style", "")+f'font-family: {tag["face"]};'
                    del tag["face"]
        return str(bs)

    def getSRT(self, lines:int = -1, css: cssutils.css.CSSStyleSheet = None, 
               add_metadata: bool = True, **kwargs):
        for tag in self.find_all():
            if tag.name:
                if tag.get("style"):
                    inline_css = self.parseStyle(tag.get("style"))
                    font_tag = self.new_tag("font")
                    wrap_in_font = False
                    for prop in inline_css:
                        prop_name = prop.name.lower()
                        prop_value = str(prop.value)
                        if prop_name == "color":
                            font_tag["color"] = "#"+"".join(get_hexrgb(prop_value))
                            wrap_in_font = True
                        elif prop_name == "font-size":
                            font_tag["size"] = prop_value
                            wrap_in_font = True
                        elif prop_name == "font-family":
                            font_tag["face"] = prop_value
                            wrap_in_font = True
                        elif prop_name == "font-weight" and prop_value == "bold":
                            tag.string.wrap(self.new_tag("b"))
                        elif prop_name == "font-style" and prop_value == "italic":
                            tag.string.wrap(self.new_tag("i"))
                        elif prop_name == "text-decoration" and prop_value == "underline":
                            tag.string.wrap(self.new_tag("u"))
                    if wrap_in_font:
                        tag.string.wrap(font_tag)
                elif tag.get("id"):
                    pass
                elif tag.get("class"):
                    pass
                tagname = tag.name.split(".")
                if len(tagname) == 2:
                    if add_metadata:
                        tag.insert_before("["+tagname[1]+"] ")
                    tag.string.wrap(self.new_tag(tagname[0]))
                tagname = tagname[0]

                if tag.name in ["b", "u", "i"]:
                    tag.string.wrap(self.new_tag(tag.name))
                    tag.unwrap()
                elif tag.name == "font":
                    font_tag = self.new_tag(tag.name)
                    if tag.get("color"):
                        font_tag["color"] = "#"+"".join(get_hexrgb(tag.get("color")))
                    if tag.get("size"):
                        font_tag["size"] = tag.get("size")
                    if tag.get("face"):
                        font_tag["face"] = tag.get("face")
                    tag.string.wrap(font_tag)
                    tag.unwrap()
                elif tag.name == "br":
                    if lines == 1:
                        tag.insert_before(" ")
                    else:
                        tag.insert_before("\n")
                    tag.unwrap()
                else:
                    tag.unwrap()

        return str(self)

    def getTTML(self, lines:int = -1, css: cssutils.css.CSSStyleSheet = None, 
                add_metadata: bool = True, **kwargs):
        for tag in self.find_all():
            if tag.name:
                if tag.get("style"):
                    inline_css = self.parseStyle(tag.get("style"))
                    for prop in inline_css:
                        prop_name = prop.name.lower().split("-")
                        prop_name = "tts:"+prop_name[0]+"".join(i.capitalize() for i in prop_name[1:])
                        if prop.name.lower() in ["color", "background-color"]:
                            tag[prop_name] = "#"+"".join(get_hexrgb(prop.value))
                        else:
                            tag[prop_name] = str(prop.value)
                    del tag["style"]
                if tag.name == "br" and lines == 1:
                    tag.insert_before(" ")
                    tag.unwrap()
        return str(self)         
    
    def getSUB(self, lines:int = -1, css: cssutils.css.CSSStyleSheet = None, 
               add_metadata: bool = True, **kwargs):
        text_lines = list(self.get_lines())
        index = 0
        y = {"bold":False, "italic": False, "underline":False}
        props = {"color":False, "size":False, "font":False}
        for tag in self.find_all():
            if tag.name:
                if tag.get("style"):
                    inline_css = self.parseStyle(tag.get("style"))
                    for prop in inline_css:
                        prop_name = prop.name.lower()
                        prop_value = str(prop.value)
                        if prop_name == "color" and not props["color"]:
                            props["color"] = True
                            text_lines[index] = "{C:$"+"".join(reversed(get_hexrgb(prop_value)))+"}"+text_lines[index]
                        elif prop_name == "font-size"and not props["size"]:
                            props["size"] = True
                            text_lines[index] = "{S:"+prop_value+"}"+text_lines[index]
                        elif prop_name == "font-family"and not props["font"]:
                            props["font"] = True
                            text_lines[index] = "{F:"+prop_value+"}"+text_lines[index]
                        elif prop_name == "font-weight" and prop_value == "bold":
                            y["bold"] = True
                        elif prop_name == "font-style" and prop_value == "italic":
                            y["italic"] = True
                        elif prop_name == "text-decoration" and prop_value == "underline":
                            y["underline"] = True
                if tag.name == "b":
                    y["bold"] = True
                elif tag.name == "i":
                    y["italic"] = True
                elif tag.name == "u":
                    y["underline"] = True
                elif tag.name == "br":
                    props = {"color":False, "size":False, "font":False}
                    if sum(y.values()):
                        print("adding style")
                        text_lines[index] = "{Y:"+",".join(style[0] for style, value in y.items() if value)+"}"+text_lines[index]
                        y = {"bold":False, "italic": False, "underline":False}
                    index += 1
        if sum(y.values()):
            text_lines[index] = "{Y:"+",".join(style[0] for style, value in y.items() if value)+"}"+text_lines[index]
        if lines == 1:
            return " ".join(text_lines)
        return "|".join(text_lines)
    
    def getVTT(self, lines:int = -1, css: cssutils.css.CSSStyleSheet = None,
               add_metadata: bool = True, **kwargs):
        for tag in self.find_all():
            if tag.name:
                if tag.name == "br":
                    if lines == 1:
                        tag.insert_before(" ")
                    else:
                        tag.insert_before("\n")
                    tag.unwrap()
        return self.get_text()

    