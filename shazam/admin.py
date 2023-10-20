from django.contrib import admin
from django.contrib.auth.models import Group, User
# Register your models here.

#remove group
admin.site.unregister(Group)

# Extand user model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]

# remove initial users
admin.site.unregister(User)

admin.site.register(User, UserAdmin)
