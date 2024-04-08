from abc import ABC, abstractmethod
from typing import List, Set
# from project.influencers import BaseInfluencer


class BaseCampaign(ABC):
    used_ids: Set[int] = set()

    def __init__(
        self,
        campaign_id: int,
        brand: str,
        budget: float,
        required_engagement: float
    ) -> None:

        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers: List = []  # FIX TYPING

    @property
    def campaign_id(self) -> int:
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id: int) -> None:
        if campaign_id <= 0:
            raise ValueError(
                "Campaign ID must be a positive integer greater than zero."
            )

        if campaign_id in self.used_ids:
            raise ValueError(
                f"Campaign with ID {campaign_id} already exists. "
                f"Campaign IDs must be unique."
            )

        self.used_ids.add(campaign_id)
        self.__campaign_id = campaign_id

    @property
    @abstractmethod
    def eligibility_coefficient(self) -> float: ...

    def check_eligibility(self, engagement_rate: float) -> bool:
        return engagement_rate >= (
            self.eligibility_coefficient * self.required_engagement
        )
