from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Thunder(models.Model):
    user = models.ForeignKey(User, related_name="thunder", on_delete=models.CASCADE)
    text = models.CharField(max_length=313)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user}"
            f"({self.created_at:%Y-%m-%d %H:%M})"
        )


#create profile for users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hunters = models.ManyToManyField('self', related_name="hunted_by", symmetrical=False, blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username
