from django.contrib import admin

from accounts.models import UserExtended, Notification

# Register your models here.
admin.site.register(UserExtended)
admin.site.register(Notification)
