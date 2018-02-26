from django.contrib import admin

from .models import UserData
from .models import UserProfile


class UserDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserData._meta.fields]
    exclude = ('password',)

    class Meta:
        model = UserData


admin.site.register(UserData, UserDataAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]

    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
