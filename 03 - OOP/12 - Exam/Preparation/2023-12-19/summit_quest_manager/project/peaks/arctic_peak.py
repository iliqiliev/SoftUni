from typing import List, Optional
from project.peaks import BasePeak


class ArcticPeak(BasePeak):
    def get_recommended_gear(self) -> List[str]:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self) -> Optional[str]:
        if self.elevation < 2000:
            return None

        if self.elevation <= 3000:
            return "Advanced"

        return "Extreme"
