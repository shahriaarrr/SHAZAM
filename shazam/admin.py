from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

#remove group
admin.site.unregister(Group)
