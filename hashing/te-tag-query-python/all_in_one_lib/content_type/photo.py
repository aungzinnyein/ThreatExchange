#!/usr/bin/env python

"""
Wrapper around the video content type.
"""
import typing as t

from ..signal_type import md5, pdq
from ..signal_type.base import SignalType
from .base import ContentType


class PhotoContent(ContentType):
    """
    Content that contains static visual imagery.

    Examples might be:
      * jpeg
      * png
      * gif (non-animated)
      * frames from videos
      * thumbnails of videos
    """

    @classmethod
    def get_signal_types(cls) -> t.List[t.Type[SignalType]]:
        return [md5.PhotoMD5Signal, pdq.PdqSignal]
