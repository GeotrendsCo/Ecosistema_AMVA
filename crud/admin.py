from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# from .models import userAttributes
from .models import Profile

class profileInLine (admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class customizedUserAdmin (UserAdmin):
    inlines = [profileInLine]

admin.site.unregister(User)
admin.site.register(User, customizedUserAdmin)

# Import admin panel administration
# admin.site.register(userAttributes)
# admin.site.register(Profile)

