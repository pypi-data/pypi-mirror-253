import io
import re
import langcodes 

from .block import Block, BlockType
from .captionsFormat import CaptionsFormat, captionsDetector, captionsReader, captionsWriter
from .microTime import MicroTime as MT


EXTENSIONS = [".sub"]
PATTERN = r"\{.*?\}"


@staticmethod
@captionsDetector
def detectSUB(content: str | io.IOBase) -> bool:
    r"""
    Used to detect MicroDVD caption format.

    It returns True if:
     - the start of a first line in a file matches regex `^{\d+}{\d+}`
    """
    line = content.readline()
    if re.match(r"^{\d+}{\d+}", line) or line.startswith(r"{DEFAULT}"):
        return True
    return False


def formatLine(self, pattern):
    start = ""
    end = ""
    font_vars = []
    _class = ""
    for control_code in pattern:
        control_code = control_code.strip("{} ").split(":")
        if len(control_code) != 2:
            continue
        control_code, value = control_code[0], control_code[1]
        control_code = control_code.upper()
        if control_code == "Y":
            value = value.split(",")
            for i in value:
                if i == "i":
                    start += "<i>"
                    end += "</i>"
                elif i == "b":
                    start += "<i>"
                    end += "</i>"
                elif i == "u":
                    start += "<i>"
                    end += "</i>"
                elif i == "s":
                    start += "<i>"
                    end += "</i>"
        elif control_code == "F":
            font_vars.append("font-family:"+value)
        elif control_code == "S":
            font_vars.append("font-size:"+value)
        elif control_code == "C":
            font_vars.append("color:#"+value[-2:]+value[-4:-2]+value[-6:-4])
        elif control_code == "H":
            self.add_metadata("default", Block(BlockType.METADATA, id="default",
                                               Language=langcodes.find(value).language))
        else:
            # control code 'P' has mixed info of how it works, ommited for now
            # there appears to also be 'o' 
            if "micro_dvd" not in self.options:
                self.options["micro_dvd"] = {
                    "control_codes": dict(),
                    "counter": 0
                }
            if not _class:
                _class = f"micro_dvd_{self.options['micro_dvd']['counter']}"
                self.options["micro_dvd"]["counter"] += 1
                self.options["micro_dvd"]["control_codes"][_class] = dict()
            self.options["micro_dvd"]["control_codes"][_class][control_code] = value
    if font_vars:
        if _class:
            _class = f"class='{_class}'"
        start += f"<p {_class}style='"+";".join(font_vars)+";'>"
        end += "</p>"
    return start, end


@captionsReader
def readSUB(self, content: str | io.IOBase, languages: list[str] = None, **kwargs):
    if not self.options.get("frame_rate"):
        self.options["frame_rate"] = kwargs.get("frame_rate") or 25
    frame_rate = kwargs.get("frame_rate") or self.options.get("frame_rate")

    if not self.options.get("blocks"):
        self.options["blocks"] = []

    line = content.readline().strip()
    while line:
        if line.startswith(r"{DEFAULT}"):
            self.options["blocks"].append(Block(BlockType.STYLE, style=line))
        else:
            lines = line.split("|")
            params = re.findall(PATTERN, lines[0])
            start = MT.fromSUBTime(params[0].strip("{} "), frame_rate)
            end = MT.fromSUBTime(params[1].strip("{} "), frame_rate)
            caption = Block(BlockType.CAPTION, start_time=start, end_time=end,
                            style=[p.strip("{}") for p in params[2:]])
            for counter, line in enumerate(lines):
                start, end = formatLine(self, re.findall(PATTERN, line))
                line = start+re.sub(PATTERN, "", line)+end
                if len(languages) > 1:
                    caption.append(line, languages[counter])
                else:
                    caption.append(line, languages[0])
            self.append(caption)
        line = content.readline().strip()


@captionsWriter("SUB", "getSUB", "|")
def saveSUB(self, filename: str, languages: list[str] = None, generator: list = None, 
            file: io.FileIO = None, **kwargs):
    frame_rate = kwargs.get("frame_rate") or self.options.get("frame_rate") or 25
    index = 1
    for text, data in generator:
        if data.block_type != BlockType.CAPTION:
            continue
        elif index != 1:
            file.write("\n")
        file.write("{"+data.start_time.toSUBTime(frame_rate)+"}{"+data.end_time.toSUBTime(frame_rate)+"}")
        file.write("|".join(i for i in text))
        index += 1


class MicroDVD(CaptionsFormat):
    """
    MicroDVD

    Read more about it https://en.wikipedia.org/wiki/MicroDVD

    Example:

    with MicroDVD("path/to/file.sub") as sub:
        sub.saveSRT("file")
    """
    detect = staticmethod(detectSUB)
    _read = readSUB
    _save = saveSUB

    from .lrc import saveLRC
    from .sami import saveSAMI
    from .srt import saveSRT
    from .ttml import saveTTML
    from .usf import saveUSF
    from .vtt import saveVTT
