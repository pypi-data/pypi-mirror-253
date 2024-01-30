from .models import Invitation
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UsernameField
from django.utils.translation import gettext as _
from django.contrib.auth import forms as authforms
# from django.urls import reverse

User = get_user_model()


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ["sender", "recipient_email"]


class DashboardSelectionForm(forms.Form):
    checked_ids = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, required=False
    )
    action = forms.ChoiceField(choices=[("delete", _("Delete"))], required=False)

    def __init__(
        self,
        *args,
        user_choices=User.objects.all().values_list("id", "username"),
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.fields["checked_ids"].choices = list(user_choices)

    def clean_checked_ids(self):
        # ensure we received valid user id(s)
        checked_ids = self.cleaned_data.get("checked_ids", [])
        invalid_ids = []
        for user_id in checked_ids:
            try:
                User.objects.get(pk=user_id)
            except User.DoesNotExist:
                invalid_ids.append(str(user_id))

        if invalid_ids:
            raise forms.ValidationError(
                _("The following user id(s) are invalid: {}").format(
                    ", ".join(invalid_ids)
                )
            )

        return checked_ids

    def clean(self):
        cleaned_data = super().clean()

        action = cleaned_data.get("action", None)
        if not action:
            raise forms.ValidationError(_("Unspecified action"))

        checked_ids = cleaned_data.get("checked_ids", [])
        if not checked_ids:
            raise forms.ValidationError(_("At least one user should be selected"))

        if action == "delete":
            # ensure at least one superuser remains to avoid locking oneself out
            superusers = User.objects.filter(is_superuser=True)
            remaining_admins = superusers.exclude(id__in=checked_ids)
            if not remaining_admins:
                raise forms.ValidationError(_("At least one administrator must remain"))

        return cleaned_data


class PasswordResetForm(authforms.PasswordResetForm):
    def save(self, html_email_template_name="hub/pass/reset_email.j2", **kwargs):
        return super().save(html_email_template_name=html_email_template_name**kwargs)


class EditUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        field_classes = {"username": UsernameField}
