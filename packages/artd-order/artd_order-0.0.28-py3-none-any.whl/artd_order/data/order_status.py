from django.utils.translation import gettext_lazy as _

ORDER_STATUSES = (
    ("new", _("New")),
    ("in_progress", _("In progress")),
    ("done", _("Done")),
    ("canceled", _("Canceled")),
    ("closed", _("Closed")),
    ("pending_payment", _("Pending payment")),
    ("failed_payment", _("Failed payment")),
    ("success_payment", _("Success payment")),
)
