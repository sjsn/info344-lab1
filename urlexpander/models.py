from django.db import models
from django.utils import timezone

class URL(models.Model):
	url = models.CharField(max_length = 250)
	date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.url
