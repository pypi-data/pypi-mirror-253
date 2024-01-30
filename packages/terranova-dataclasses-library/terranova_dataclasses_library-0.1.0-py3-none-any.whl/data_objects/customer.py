from dataclasses import dataclass

from dataclasses_json import dataclass_json

from data_objects.enums.classification import Classification
from data_objects.enums.rank import Rank


@dataclass_json
@dataclass
class Customer:
    name:str 
    classification:Classification
    rank:Rank

    
