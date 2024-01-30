from django.contrib import admin

# from oidc_provider.models import Token, RSAKey, Client, Code
from django.contrib.auth import get_user_model
from .models import Invitation
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Invitation)

# # unregister oidc models
# admin.site.unregister(RSAKey)
# admin.site.unregister(Client)
# admin.site.unregister(Token)
# admin.site.unregister(Code)
