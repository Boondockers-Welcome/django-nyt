from django.contrib import admin
from django.utils.translation import gettext as _
from django_nyt import models, settings


class SettingsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('user', 'interval',)
    search_fields = ['user__username']


class SubscriptionAdmin(admin.ModelAdmin):
    raw_id_fields = ('settings', 'latest')
    list_display = ('display_user', 'notification_type', 'display_interval',)
    search_fields = ['settings__user__username']

    def display_user(self, instance):
        return instance.settings.user
    display_user.short_description = _("user")

    def display_interval(self, instance):
        return instance.settings.interval
    display_interval.short_description = _("interval")


class NotificationAdmin(admin.ModelAdmin):

    raw_id_fields = ('user', 'subscription')
    list_display = ('user', 'created', 'display_type', 'is_viewed', 'message')
    search_fields = ['user__username__iexact']

    def display_type(self, instance):
        return instance.subscription.notification_type
    display_type.short_description = _("type")


if settings.ENABLE_ADMIN:
    admin.site.register(models.NotificationType)
    admin.site.register(models.Notification, NotificationAdmin)
    admin.site.register(models.Settings, SettingsAdmin)
    admin.site.register(models.Subscription, SubscriptionAdmin)
