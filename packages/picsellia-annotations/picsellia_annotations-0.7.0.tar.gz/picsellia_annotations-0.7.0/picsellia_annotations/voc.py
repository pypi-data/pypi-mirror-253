from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class Size(BaseModel):
    width: int
    height: int
    depth: int


class Source(BaseModel):
    database: str


class BndBox(BaseModel):
    xmin: Union[int, float]
    xmax: Union[int, float]
    ymin: Union[int, float]
    ymax: Union[int, float]


class Object(BaseModel):
    name: str
    pose: Optional[str]
    truncated: Optional[int]
    difficult: Optional[int]
    occluded: Optional[int]
    bndbox: Optional[BndBox]
    polygon: Optional[Dict[str, Union[int, float]]]

    def is_rle(self) -> bool:
        return False

    def is_polygon(self) -> bool:
        return self.polygon is not None

    def is_rectangle(self) -> bool:
        return self.polygon is None and self.bndbox is not None

    def polygon_to_list_coordinates(self) -> List[List[int]]:
        if not self.is_polygon():
            raise ValueError("Not a polygon")

        coords = []
        for i in range(1, 1 + len(self.polygon) // 2):
            x = "x" + str(i)
            y = "y" + str(i)
            if x not in self.polygon or y not in self.polygon:
                raise ValueError("{} or {} not found in this polygon.".format(x, y))

            coords.append([int(self.polygon[x]), int(self.polygon[y])])

        return coords


class Annotation(BaseModel):
    filename: str
    object: Union[Object, List[Object]]
    path: Optional[str]
    folder: Optional[str]
    source: Optional[Source]
    size: Optional[Size]
    segmented: Optional[int]


class PascalVOCFile(BaseModel):
    annotation: Annotation
