from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json
from osgeo import ogr
from osgeo.osr import SpatialReference


from data_objects.enums.background_color import BackgroundColor
from data_objects.enums.coordinate_systems import CoordinateSystems
from data_objects.enums.product_type import ProductType
from data_objects.formats.formats import Formats
from data_objects.resolution import Resolution
from data_objects.structs.date_range import DateRange


@dataclass_json
@dataclass(kw_only=True)
class Product():
    id: Optional[str] = None
    name: Optional[str] = None
    version:  Optional[int] = None 
    data_path: Optional[str] = None
    type: Optional[ProductType] =  ProductType.ORTHOPHOTO
    coordinate_system: Optional[CoordinateSystems] = None
    format: Optional[Formats] = None
    background: Optional[BackgroundColor] = None
    resolution: Optional[Resolution] = None
    wkt_polygon: Optional[str] = None
    update_date_range: Optional[DateRange] = None

    def get_polygon_as_geometry(self) -> ogr.Geometry:
        spatial_ref = SpatialReference()
        spatial_ref.ImportFromEPSG(self.coordinate_system.value)
        return ogr.CreateGeometryFromWkt(self.wkt_polygon, spatial_ref)
    
    def set_geometry_as_polygon(self, geometry: ogr.Geometry):
        self.wkt_polygon = geometry.ExportToWkt()
    
    def clone(self) -> "Product":
        return Product.from_json(self.to_json())
    
