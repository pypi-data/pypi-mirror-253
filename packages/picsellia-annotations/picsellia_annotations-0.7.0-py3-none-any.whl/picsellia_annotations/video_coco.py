from typing import List

from pydantic import BaseModel

from .coco import Annotation, COCOFile, Image


class ExtendedImage(Image):
    video_id: int = None
    frame_id: int = None
    file_name: str = None


class Video(BaseModel):
    id: int
    file_name: str


class Attributes(BaseModel):
    occluded: bool = False
    rotation: float = None
    track_id: int = None
    keyframe: bool = False
    frame_id: int = None


class VideoAnnotation(Annotation):
    video_id: int = None
    attributes: Attributes = None


class VideoCOCOFile(COCOFile):
    videos: List[Video] = None
    images: List[ExtendedImage]
    annotations: List[VideoAnnotation]
