import io

from .block import Block, BlockType
from .captionsFormat import CaptionsFormat, captionsDetector, captionsReader, captionsWriter
from .microTime import MicroTime as MT
from bs4 import BeautifulSoup


EXTENSIONS = [".sami"]


@staticmethod
@captionsDetector
def detectSAMI(content: str | io.IOBase) -> bool:
    """
    Used to detect Synchronized Accessible Media Interchange caption format.

    It returns True if:
     - the first line starts with <SAMI>
    """
    if content.readline().lstrip().startswith("<SAMI>"):
        return True
    return False


@captionsReader
def readSAMI(self, content: str | io.IOBase, languages: list[str] = None, **kwargs):
    raise ValueError("Not Implemented")


@captionsWriter("SAMI", "getSAMI")
def saveSAMI(self, filename: str, languages: list[str] = None, generator: list = None, 
             file: io.FileIO = None, **kwargs):
    raise ValueError("Not Implemented")


class SAMI(CaptionsFormat):
    """
    Synchronized Accessible Media Interchange

    Read more about it https://learn.microsoft.com/en-us/previous-versions/windows/desktop/dnacc/understanding-sami-1.0

    Example:

    with SAMI("path/to/file.sami") as sami:
        sami.saveSRT("file")
    """
    detect = staticmethod(detectSAMI)
    read = readSAMI
    save = saveSAMI

    from .lrc import saveLRC
    from .srt import saveSRT
    from .sub import saveSUB
    from .ttml import saveTTML
    from .usf import saveUSF
    from .vtt import saveVTT
