from django.db import models
from django.utils.translation import gettext_lazy as _

class UserStatus(models.TextChoices):
    VERIFIED = 'verified', _('Verified')
    UNVERIFIED = 'unverified', _('Unverified')