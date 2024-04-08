from project.campaigns import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    DEFAULT_BUDGET: float = 5000.0

    def __init__(
        self, campaign_id: int, brand: str, required_engagement: float
    ) -> None:

        super().__init__(
            campaign_id, brand, self.DEFAULT_BUDGET, required_engagement
        )

    @property
    def eligibility_coefficient(self) -> float:
        return 1.2
