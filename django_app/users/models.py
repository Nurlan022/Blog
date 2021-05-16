from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

SEX_OPTIONS = (
	('U', 'Unsure'),
	('F', 'Female'),
	('M', 'Male')
)

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	sex = models.CharField(max_length=10,default='U',choices=SEX_OPTIONS)
	birth_day = models.DateField(default=timezone.now)
	


	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)
