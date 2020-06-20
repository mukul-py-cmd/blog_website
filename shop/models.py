from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
	product_name = models.CharField(max_length = 50)
	product_desc = models.CharField(max_length = 300)
	pub_date = models.DateTimeField(default =timezone.now)

	def __str__(self):
		return "product_name {0}".format(self.product_name)