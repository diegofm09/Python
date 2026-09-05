from dataclasses import dataclass

@dataclass(frozen=True)
class GPSPoint:
    label: str
    latitude: float
    longitude: float

    def __post_init__(self):

        object.__setattr__(self, "label", self.label.strip())
        
        if not self.label:
            raise ValueError

        if self.latitude < -90.0 or self.latitude > 90.0:
            raise ValueError

        
