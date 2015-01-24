from django.db import models

# Create your models here.
class userinfo(models.Model):
	user_id = models.CharField(max_length=32)
	