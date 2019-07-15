import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Topics(models.Model):
	def __str__(self):
		return self.topic_title

	def was_added_recently(self):
		return self.topic_date > timezone.now() - datetime.timedelta(days=1)

	topic_title = models.CharField(max_length = 100)
	topic_text = models.TextField()
	topic_date = models.DateField('create_date')