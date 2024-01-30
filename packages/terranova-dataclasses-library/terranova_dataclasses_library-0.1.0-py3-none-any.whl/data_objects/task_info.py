from dataclasses import dataclass


@dataclass(frozen = True)
class TaskInfo:
    assembly: str
    _class: str
    defenitionPath: str
    name: str
