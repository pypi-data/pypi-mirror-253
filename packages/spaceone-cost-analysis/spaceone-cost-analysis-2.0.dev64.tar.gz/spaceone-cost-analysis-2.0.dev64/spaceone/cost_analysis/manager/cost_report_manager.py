import logging
from typing import Tuple
from mongoengine import QuerySet

from spaceone.core.manager import BaseManager
from spaceone.cost_analysis.model.cost_report.database import CostReport

_LOGGER = logging.getLogger(__name__)


class CostReportManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cost_report_model = CostReport

    def get_cost_report(
        self, domain_id: str, cost_report_id: str, workspace_id: str = None
    ) -> CostReport:
        conditions = {
            "cost_report_id": cost_report_id,
            "domain_id": domain_id,
        }
        if workspace_id:
            conditions["workspace_id"] = workspace_id

        return self.cost_report_model.get(**conditions)

    def filter_cost_reports(self, **conditions) -> QuerySet:
        return self.cost_report_model.filter(**conditions)

    def list_cost_reports(self, query: dict) -> Tuple[QuerySet, int]:
        return self.cost_report_model.query(**query)

    def stat_cost_reports(self, query: dict) -> dict:
        return self.cost_report_model.stat(**query)
