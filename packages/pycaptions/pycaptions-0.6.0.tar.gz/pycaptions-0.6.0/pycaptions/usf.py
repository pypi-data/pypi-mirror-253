import io

from .block import Block, BlockType
from .captionsFormat import CaptionsFormat, captionsDetector, captionsReader, captionsWriter
from .microTime import MicroTime as MT


EXTENSIONS = [".usf"]


@staticmethod
@captionsDetector
def detectUSF(content: str | io.IOBase) -> bool:
    """
    Used to detect Universal Subtitle Format caption format.

    It returns True if:
     - the first line starts with <USFSubtitles
    """
    if content.readline().lstrip().startswith("<USFSubtitles"):
        return True
    return False

@captionsReader
def readUSF(self, content: str | io.IOBase, languages: list[str] = None, **kwargs):
    raise ValueError("Not Implemented")

@captionsWriter("USF", "getUSF")
def saveUSF(self, filename: str, languages: list[str] = None, generator: list = None, 
            file: io.FileIO = None, **kwargs):
    raise ValueError("Not Implemented")


class USF(CaptionsFormat):
    """
    Universal Subtitle Format

    Read more about it https://en.wikipedia.org/wiki/Universal_Subtitle_Format

    Example:

    with USF("path/to/file.usf") as usf:
        usf.saveSRT("file")
    """
    detect = staticmethod(detectUSF)
    read = readUSF
    save = saveUSF

    from .lrc import saveLRC
    from .sami import saveSAMI
    from .srt import saveSRT
    from .sub import saveSUB
    from .ttml import saveTTML
    from .vtt import saveVTT   
