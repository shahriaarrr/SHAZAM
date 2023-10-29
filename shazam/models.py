from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Thunder(models.Model):
    user = models.ForeignKey(User, related_name="thunder", on_delete=models.CASCADE)
    text = models.CharField(max_length=313)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="Thunder_like", blank=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return (
            f"{self.user}"
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.text}"
        )


#create profile for users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hunters = models.ManyToManyField('self', related_name="hunted_by", symmetrical=False, blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.user.username
