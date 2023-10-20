from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile
# Register your models here.

#remove group
admin.site.unregister(Group)

# add profile info into user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extand user model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

# remove initial users
admin.site.unregister(User)

#register models
admin.site.register(User, UserAdmin)


