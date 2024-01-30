from . import forms
from . import models
from .forms import InvitationForm, DashboardSelectionForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, mixins, views, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from django.views import generic, View
from django.views.generic import TemplateView
from oidc_hub.shortcuts import redirect


User = get_user_model()


class UserToolsMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("has_permission", self.request.user.is_authenticated)
        return context


class DashboardView(mixins.LoginRequiredMixin, UserToolsMixin, TemplateView):
    template_name = "hub/dashboard.j2"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            users=User.objects.all(),
            invitation_form=InvitationForm(),
            user_as_json=serializers.serialize("json", [self.request.user]),
        )
        return context

    def post(self, request, *args, **kwargs):
        # check permission
        if not request.user.is_superuser:
            # inform user about missing permission
            messages.error(request, _("Permission denied"))
            return redirect("hub:dashboard", status_code=303)

        # create form
        form = DashboardSelectionForm(request.POST)

        # validate form
        if form.is_valid():
            # retrieve user instances from cleaned checked ids
            checked_ids = form.cleaned_data["checked_ids"]
            users = User.objects.filter(pk__in=checked_ids)

            # handle delete action
            if form.cleaned_data.get("action", None) == "delete":
                # delete users and aggregate deleted usernames
                # @TODO: add a confirmation page
                deleted_usernames = []
                for user in users:
                    deleted_usernames.append(user.username)
                    user.delete()

                # inform user about changes
                messages.success(
                    request,
                    _("The following users have been deleted: {}").format(
                        ", ".join(deleted_usernames)
                    ),
                )

            return redirect("hub:dashboard")
        else:
            # inform user about errors
            for field, errors in form.errors.items():
                for error in errors:
                    print(field, error)
                    messages.error(request, error)
            return redirect("hub:dashboard", status_code=303)


class EditUserView(
    LoginRequiredMixin, UserToolsMixin, UserPassesTestMixin, generic.UpdateView
):
    model = User
    form_class = forms.EditUserForm
    template_name = "hub/users/edit.j2"
    success_url = reverse_lazy("hub:dashboard")

    def test_func(self):
        return self.request.user.is_superuser or self.get_object() == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # append form to send reset password email to a user if admin privileges
        # are granted to the request user
        form = self.get_form()

        reset_text = _('send a reset link')

        if self.request.user.is_superuser and self.request.user != self.object:
            # POST the password reset form to send a link to 
            pass_reset_form = forms.PasswordResetForm({"email": self.object.email})
            pass_reset_form.fields["email"].widget.input_type = "hidden"

            send_reset_link_form = render_to_string(
                "hub/users/pass_reset_form.j2",
                {
                    "form": pass_reset_form,
                },
                request=self.request,
            ).strip("\n")

            form.fields["password"].help_text = _(
                "Raw passwords are not stored, so there is no way to see this "
                "user’s password, but you can {} instead."
            ).format(
                f"<button type='submit' form='send-reset-link' class='link'>{reset_text}</button>"
            )

            context["form"] = form
            context["send_reset_link_form"] = mark_safe(send_reset_link_form)

        if self.request.user == self.object:

            change_pass_text = _("change your password")

            form.fields["password"].help_text = _(
                "Raw passwords are not stored, so there is no way to display your "
                "password, but you can {}."
            ).format(f"<a href='{reverse('hub:pass_change')}'>{change_pass_text}</a>")

            context["form"] = form

        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get(pk=self.kwargs.get("user_id", self.request.user.pk))


class SignUpView(generic.CreateView):
    """
    A view to create new accounts
    """

    model = User
    fields = ("username", "password")

    template_name = "hub/signup.j2"

    invalid_token_url = reverse_lazy("hub:invalid_token")
    success_url = reverse_lazy("hub:signin")

    def get(self, request, *args, **kwargs):
        invitation = self.get_invitation()
        if not invitation:
            return HttpResponseRedirect(self.invalid_token_url)

        self.object = None
        return self.render_to_response(self.get_context_data(token=invitation.token))

    def post(self, request, *args, **kwargs):
        # token validation
        invitation = self.get_invitation()
        if not invitation:
            return HttpResponseRedirect(self.invalid_token_url)

        form = self.get_form()

        if form.is_valid():
            # update form instance email using the invitation
            form.instance.email = invitation.recipient_email
            # turn plain-text password into a hash for database storage
            form.instance.set_password(form.instance.password)
            # save new user object
            self.object = form.save()
            # delete the invitation
            invitation.delete()
            # log the user in
            login(self.request, self.object)
            # return success redirect
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def get_invitation(self):
        try:
            token = self.request.GET.get("token", None)
            return models.Invitation.objects.get(token=token)
        except Exception:
            return None

    def dispatch(self, request, *args, **kwargs):
        """
        Redirect any authenticated user to the dashboard.
        """
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("hub:dashboard"))
        return super().dispatch(request, *args, **kwargs)


class PasswordResetView(views.PasswordResetView):
    success_url = reverse_lazy("hub:dashboard")
    template_name = "hub/pass/reset.j2"
    email_template_name = "hub/pass/reset_email.j2"

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        messages.success(
            self.request,
            _("We've sent a mail with instructions to reset this user's password. It should be received shortly."),
        )
        return super().form_valid(form)


class PasswordResetDoneView(UserToolsMixin, views.PasswordResetDoneView):
    template_name = "hub/pass/reset_done.j2"


class PasswordResetConfirmView(UserToolsMixin, views.PasswordResetConfirmView):
    post_reset_login = True
    reset_url_token = "confirm"
    success_url = reverse_lazy("hub:dashboard")
    # template_name = "hub/pass/reset_confirm.j2"


class PasswordChangeView(UserToolsMixin, views.PasswordChangeView):
    success_url = reverse_lazy("hub:pass_change_done")
    template_name = "hub/pass/change.j2"


class PasswordChangeDoneView(UserToolsMixin, views.PasswordChangeDoneView):
    template_name = "hub/pass/change_done.j2"


class InvitationView(mixins.LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            return self.post(request, *args, **kwargs)
        else:
            return HttpResponseNotAllowed(["POST"])

    def post(self, request, *args, **kwargs):
        # init form
        form = InvitationForm(request.POST)
        # validate form data
        if form.is_valid():
            # make sure an invitation object is created
            if invitation := form.save():
                # compute an email subject
                subject = _("{} sent you an invitation").format(invitation.sender.username)

                # build up a context object for rendering email content
                context = {
                    "token": invitation.token, 
                    "absolute_uri": request.build_absolute_uri(reverse("hub:signup")), 
                    "subject": subject
                }

                # render email content
                html = render_to_string("hub/emails/invitation.j2", context)
                txt = render_to_string("hub/emails/invitation.txt", context)

                try:
                    # send email to recipient
                    email = EmailMultiAlternatives(
                        subject, txt, settings.DEFAULT_FROM_EMAIL, [invitation.recipient_email]
                    )
                    email.attach_alternative(html, "text/html")
                    email.send()

                    messages.success(
                        request,
                        _("An invitation has been sent to {}").format(invitation.recipient_email),
                    )
                except Exception as e:
                    # email validation errors
                    messages.error(
                        request,
                        str(e)
                    )

            return redirect("hub:dashboard")
        else:
            # form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            return redirect("hub:dashboard")

