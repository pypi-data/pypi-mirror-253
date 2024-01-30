from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, reverse_lazy

app_name = "hub"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    # registration
    re_path(r"signup/?", views.SignUpView.as_view(), name="signup"),
    # authentication
    re_path(
        r"signin/?$",
        auth_views.LoginView.as_view(
            template_name="hub/signin.j2",
            redirect_authenticated_user=True,
            success_url=reverse_lazy("hub:dashboard"),
        ),
        name="signin",
    ),
    re_path(
        r"signout/?$",
        auth_views.LogoutView.as_view(
            template_name="hub/signout.j2",
        ),
        name="signout",
    ),
    # reset password
    re_path(r"pass/reset/?$", views.PasswordResetView.as_view(), name="pass_reset"),
    re_path(
        r"pass/reset/sent/?$",
        views.PasswordResetDoneView.as_view(),
        name="pass_reset_done",
    ),
    re_path(
        r"pass/reset/(?P<uidb64>[^.]*)/(?P<token>[^.]*)/?$",
        views.PasswordResetConfirmView.as_view(),
        name="pass_reset_confirm",
    ),
    # change password
    re_path(r"pass/change/?$", views.PasswordChangeView.as_view(), name="pass_change"),
    re_path(
        r"pass/change/success/?$",
        views.PasswordChangeDoneView.as_view(),
        name="pass_change_done",
    ),
    # invitation
    re_path(r"invitations/?$", views.InvitationView.as_view(), name="invitations"),
    re_path(
        r"users/(?P<user_id>\d+)/edit/?$",
        views.EditUserView.as_view(),
        name="edit_user",
    ),
]
