from django.contrib import admin
from . import models


@admin.register(models.OAuthToken)
class OAuthTokenAdmin(admin.ModelAdmin):
    search_fields = ['user__email', 'user__username']
    list_display = ['user', 'oauth_user_id']
    list_filter = ('expires_at',)
    raw_id_fields = ['user']


@admin.register(models.OAuthUserInfo)
class OAuthUserInfoAdmin(admin.ModelAdmin):
    search_fields = ['user__email', 'user__username', 'oauth_user_id']
    list_display = ['user', 'oauth_user_id']
    raw_id_fields = ['user']
