from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .base_action_view import BaseActionView

app_config = django_apps.get_app_config("edc_pharmacy_dashboard")


class DispensingActionView(BaseActionView):
    post_url_name = app_config.appointment_listboard_url_name
    listboard_url_name = app_config.appointment_listboard_url_name
    valid_form_actions = ["dispensing"]
    prescription_model = "edc_pharmacy.prescription"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._selected_manifest = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def process_form_action(self):
        if self.action == "dispensing":
            self.dispensing()

    def dispensing(self):
        """Adds the selected items to the selected manifest."""
        return None
