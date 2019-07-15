from django.db import models

from django.db import models
from django.utils import timezone

# Create your models here.
class Stocks(models.Model):
	def __str__(self):
		return self.stock_name + "_" + self.stock_code

	stock_name = models.CharField(max_length = 50)
	stock_code = models.CharField(max_length = 10)
	stock_buy_in_price = models.FloatField(null=False, default=0.0)