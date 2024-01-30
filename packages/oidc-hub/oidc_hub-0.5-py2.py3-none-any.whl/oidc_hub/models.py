from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class Invitation(models.Model):
    sender = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE, verbose_name=_('Sender'))
    recipient_email = models.EmailField(verbose_name=_("Email address"), unique=True)
    token = models.CharField(verbose_name=_("Token"), max_length=32, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Invitation: '{self.recipient_email}'>"

    def save(self, *args, **kwargs):
        adding = self._state.adding
        if adding:
            self.token = get_random_string(
                length=self._meta.get_field("token").max_length
            )

        super().save(*args, **kwargs)
