from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# the users info i enter
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    blog_title = models.CharField(max_length=20)
    blog_entry = models.CharField(max_length=20)
    blogger_number = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

