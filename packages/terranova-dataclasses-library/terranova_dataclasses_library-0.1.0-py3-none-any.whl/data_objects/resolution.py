from dataclasses import dataclass

from dataclasses_json import dataclass_json

from data_objects.enums.geo_units import GeoUnits


@dataclass_json
@dataclass
class Resolution:
    units: GeoUnits
    value: tuple[float,float]

    def __post_init__(self):
        if self.value is float:
            self.value = (abs(self.value),-abs(self.value))

