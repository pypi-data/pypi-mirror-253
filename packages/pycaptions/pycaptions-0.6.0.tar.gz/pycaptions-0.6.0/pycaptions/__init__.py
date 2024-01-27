__version__ = "0.6.0"

import pycaptions.srt as srt
import pycaptions.sub as sub
import pycaptions.ttml as ttml
import pycaptions.vtt as vtt

from pycaptions.captionsFormat import save_extensions
from pycaptions.microTime import MicroTime
from pycaptions.captions import Captions
from pycaptions.srt import detectSRT, SubRip
from pycaptions.sub import detectSUB, MicroDVD
from pycaptions.ttml import detectTTML, TTML
from pycaptions.vtt import detectVTT, WebVTT

supported_readers = srt.EXTENSIONS + sub.EXTENSIONS + ttml.EXTENSIONS + vtt.EXTENSIONS
supported_extensions = srt.EXTENSIONS + sub.EXTENSIONS + ttml.EXTENSIONS + vtt.EXTENSIONS
