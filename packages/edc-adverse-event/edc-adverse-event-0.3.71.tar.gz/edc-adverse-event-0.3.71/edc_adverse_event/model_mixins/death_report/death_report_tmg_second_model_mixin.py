from edc_action_item.managers import (
    ActionIdentifierModelManager,
    ActionIdentifierSiteManager,
)

from ...constants import DEATH_REPORT_TMG_SECOND_ACTION
from .death_report_tmg_model_mixin import DeathReportTmgModelMixin


class DeathReportTmgSecondManager(ActionIdentifierModelManager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(action_item__action_type__name=DEATH_REPORT_TMG_SECOND_ACTION)


class DeathReportTmgSecondSiteManager(ActionIdentifierSiteManager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(action_item__action_type__name=DEATH_REPORT_TMG_SECOND_ACTION)


class DeathReportTmgSecondModelMixin(DeathReportTmgModelMixin):
    action_name = DEATH_REPORT_TMG_SECOND_ACTION

    objects = DeathReportTmgSecondManager()

    on_site = DeathReportTmgSecondSiteManager()

    class Meta(DeathReportTmgModelMixin.Meta):
        abstract = True
        verbose_name = "Death Report TMG (2nd)"
        verbose_name_plural = "Death Report TMG (2nd)"
        indexes = DeathReportTmgModelMixin.Meta.indexes
