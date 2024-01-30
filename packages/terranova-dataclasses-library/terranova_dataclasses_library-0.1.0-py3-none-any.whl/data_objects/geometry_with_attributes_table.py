from dataclasses import dataclass

from osgeo.ogr import Geometry


@dataclass(init=False)
class GeometryWithAttributes:
    geometry: Geometry
    attributes: list[str]

    def __init__(self, geometry: Geometry, attributes: list[str] = []) -> None:
        self.geometry = geometry
        self.attributes = attributes


@dataclass(init=False)
class GeometryWithAttributesTable:
    rows: list[GeometryWithAttributes]
    attribute_columns: list[str]

    def __init__(self, rows: list[GeometryWithAttributes] = None, attributeColumns: list[str] = []) -> None:
        self.rows = []
        self.attribute_columns = attributeColumns
        if rows is not None:
            for row in rows:
                self.add(row)


    def add(self, row:GeometryWithAttributes):
        if len(row.attributes) != len(self.attribute_columns):
            raise Exception("attribute_columns and attribute values dimensions mismatch")
        self.rows.append(row)



        

    


    