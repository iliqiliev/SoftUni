class Town:

    def __init__(self, name: str) -> None:
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude: str):
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        self.longitude = longitude

    def __str__(self) -> str:
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
