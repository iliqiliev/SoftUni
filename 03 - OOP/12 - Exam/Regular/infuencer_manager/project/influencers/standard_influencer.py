from typing import Dict
from project.influencers import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    @property
    def payment_coefficient(self) -> float:
        return 0.45

    @property
    def campaign_follower_coefficient(self) -> Dict[str, float]:
        return {
            "HighBudgetCampaign": 1.2,
            "LowBudgetCampaign": 0.9,
        }
