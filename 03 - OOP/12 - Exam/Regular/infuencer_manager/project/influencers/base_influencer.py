from abc import ABC, abstractmethod
from typing import Dict, List
from project.campaigns import BaseCampaign


class BaseInfluencer(ABC):
    def __init__(
        self, username: str, followers: int, engagement_rate: float
    ) -> None:

        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: List[BaseCampaign] = []

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str) -> None:
        if not username.strip():
            raise ValueError(
                "Username cannot be empty or consist only of whitespace!"
            )

        self.__username = username

    @property
    def followers(self) -> int:
        return self.__followers

    @followers.setter
    def followers(self, followers: int) -> None:
        if followers < 0:
            raise ValueError("Followers must be a non-negative integer!")

        self.__followers = followers

    @property
    def engagement_rate(self) -> float:
        return self.__engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, engagement_rate: float) -> None:
        if not 0 <= engagement_rate <= 5:
            raise ValueError("Engagement rate should be between 0 and 5.")

        self.__engagement_rate = engagement_rate

    @property
    @abstractmethod
    def payment_coefficient(self) -> float: ...

    @property
    @abstractmethod
    def campaign_follower_coefficient(self) -> Dict[str, float]: ...

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        return campaign.budget * self.payment_coefficient

    def reached_followers(self, campaign_type: str) -> int:
        coefficient = self.campaign_follower_coefficient[campaign_type]

        return int(self.followers * self.engagement_rate * coefficient)

    def display_campaigns_participated(self) -> str:
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."

        result = [
            f"{self.__class__.__name__} :) {self.username} :) participated "
            "in the following campaigns:",

            *(
                f"  - Campaign ID: {campaign.campaign_id}, "
                f"Brand: {campaign.brand}, Reached followers: "
                f"{self.reached_followers(campaign.__class__.__name__)}"
                for campaign in self.campaigns_participated
            )
        ]

        return "\n".join(result)
