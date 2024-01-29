from django.conf import settings
from edc_navbar import Navbar, NavbarItem, site_navbars

no_url_namespace = True if settings.APP_NAME == "edc_pharmacy_dashboard" else False

navbar = Navbar(name="pharmacy_dashboard")


navbar.register(
    NavbarItem(
        name="prescribe",
        title="prescribe",
        label="Prescribe",
        fa_icon="fa-pencil",
        no_url_namespace=no_url_namespace,
        codename="edc_navbar.nav_pharmacy_prescribe",
        url_name="edc_pharmacy_dashboard:prescribe_listboard_url",
    )
)

navbar.register(
    NavbarItem(
        name="dispense",
        title="dispense",
        label="Dispense",
        fa_icon="fa-notes-medical",
        no_url_namespace=no_url_namespace,
        codename="edc_navbar.nav_pharmacy_dispense",
        url_name="edc_pharmacy_dashboard:dispense_listboard_url",
    )
)

navbar.register(
    NavbarItem(
        name="pharmacy",
        fa_icon="fa-medkit",
        no_url_namespace=no_url_namespace,
        codename="edc_navbar.nav_pharmacy_section",
        url_name="edc_pharmacy_dashboard:home_url",
    )
)


site_navbars.register(navbar)
