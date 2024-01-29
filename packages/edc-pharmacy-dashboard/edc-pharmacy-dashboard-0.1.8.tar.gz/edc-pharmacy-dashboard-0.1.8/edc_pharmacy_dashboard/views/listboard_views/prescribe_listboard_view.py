from __future__ import annotations

from typing import TYPE_CHECKING, Any

from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from edc_navbar import NavbarViewMixin

from ..listboard_filters import PrescriptionListboardViewFilters
from .base_listboard import BaseListboardView

if TYPE_CHECKING:
    from django.db.models import Q

app_config = django_apps.get_app_config("edc_pharmacy_dashboard")


class PrescribeListboardView(NavbarViewMixin, BaseListboardView):
    navbar_selected_item = "prescribe"
    navbar_name = "pharmacy_dashboard"

    listboard_template_name = app_config.prescribe_listboard_template_name
    listboard_url_name = app_config.prescribe_listboard_url_name
    listboard_view_filters = PrescriptionListboardViewFilters()

    model = "edc_pharmacy.prescription"

    show_all = True

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        kwargs.update(listboard_url_name=self.listboard_url_name)
        return super().get_context_data(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset_filter_options(self, request, *args, **kwargs) -> tuple[Q, dict]:
        q_object, options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get("q"):
            options.update(subject_identifier=kwargs.get("q"))
        return q_object, options
