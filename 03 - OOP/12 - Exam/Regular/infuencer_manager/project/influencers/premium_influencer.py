from typing import Dict
from project.influencers import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    @property
    def payment_coefficient(self) -> float:
        return 0.85

    @property
    def campaign_follower_coefficient(self) -> Dict[str, float]:
        return {
            "HighBudgetCampaign": 1.5,
            "LowBudgetCampaign": 0.8,
        }
