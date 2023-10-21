from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#create profile for users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hunters = models.ManyToManyField('self', related_name="hunted_by", symmetrical=False, blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username
