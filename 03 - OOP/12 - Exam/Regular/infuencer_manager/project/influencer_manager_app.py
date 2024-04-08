from collections import defaultdict
from typing import Dict, List, Optional, Type, Union
from project.campaigns import (
    BaseCampaign, HighBudgetCampaign, LowBudgetCampaign
)
from project.influencers import (
    BaseInfluencer, PremiumInfluencer, StandardInfluencer
)


CampaignHasDefaultBudgetT = Type[Union[HighBudgetCampaign, LowBudgetCampaign]]


class InfluencerManagerApp:
    valid_influencers: Dict[str, Type[BaseInfluencer]] = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer,
    }

    valid_campaigns: Dict[str, CampaignHasDefaultBudgetT] = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign,
    }

    def __init__(self) -> None:
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(
        self,
        influencer_type: str,
        username: str,
        followers: int,
        engagement_rate: float
    ) -> str:

        if influencer_type not in self.valid_influencers:
            return f"{influencer_type} is not an allowed influencer type."

        if any(
            influencer.username == username for influencer in self.influencers
        ):
            return f"{username} is already registered."

        influencer_class = self.valid_influencers[influencer_type]
        influencer = influencer_class(username, followers, engagement_rate)
        self.influencers.append(influencer)

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(
        self,
        campaign_type: str,
        campaign_id: int,
        brand: str,
        required_engagement: float
    ) -> str:

        if campaign_type not in self.valid_campaigns:
            return f"{campaign_type} is not a valid campaign type."

        if any(
            campaign.campaign_id == campaign_id for campaign in self.campaigns
        ):
            return f"Campaign ID {campaign_id} has already been created."

        campaign_class = self.valid_campaigns[campaign_type]
        campaign = campaign_class(campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)

        return (
            f"Campaign ID {campaign_id} for {brand} "
            f"is successfully created as a {campaign_type}."
        )

    def _get_influencer(self, username: str) -> BaseInfluencer:
        for influencer in self.influencers:
            if influencer.username == username:
                return influencer

        raise ValueError(f"Influencer '{username}' not found.")

    def _get_campaign(self, campaign_id: int) -> BaseCampaign:
        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return campaign

        raise ValueError(f"Campaign with ID {campaign_id} not found.")

    def participate_in_campaign(
        self, influencer_username: str, campaign_id: int
    ) -> Optional[str]:

        try:
            influencer = self._get_influencer(influencer_username)
            campaign = self._get_campaign(campaign_id)

        except ValueError as error:
            return str(error)

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (
                f"Influencer '{influencer_username}' does not meet the "
                f"eligibility criteria for the campaign with ID {campaign_id}."
            )

        influencer_payment = influencer.calculate_payment(campaign)

        if influencer_payment <= 0:
            return None

        campaign.approved_influencers.append(influencer)
        campaign.budget -= influencer_payment
        influencer.campaigns_participated.append(campaign)

        return (
            f"Influencer '{influencer_username}' has successfully "
            f"participated in the campaign with ID {campaign_id}."
        )

    def calculate_total_reached_followers(self) -> Dict[BaseCampaign, int]:
        result = {}

        for campaign in self.campaigns:
            if not campaign.approved_influencers:
                continue

            result[campaign] = sum(
                influencer.reached_followers(campaign.__class__.__name__)
                for influencer in campaign.approved_influencers
            )

        return result

    def influencer_campaign_report(self, username: str) -> str:
        return self._get_influencer(username).display_campaigns_participated()

    def campaign_statistics(self) -> str:
        followers_info = defaultdict(
            int, self.calculate_total_reached_followers()
        )

        sorted_campaigns = sorted(
            self.campaigns,
            key=lambda campaign: (
                len(campaign.approved_influencers),
                -campaign.budget
            )
        )

        result = [
            "$$ Campaign Statistics $$",
            *(
                f"  * Brand: {campaign.brand}, "
                f"Total influencers: {len(campaign.approved_influencers)}, "
                f"Total budget: ${campaign.budget:.2f}, "
                f"Total reached followers: {followers_info[campaign]}"
                for campaign in sorted_campaigns
            )
        ]

        return "\n".join(result)
