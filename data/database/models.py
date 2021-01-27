from django.db import models
from datetime import date
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class Table(models.Model):
	event = models.CharField(max_length=140, default="")
	start = models.DateField()
	end = models.DateField()

	def __str__(self):
		return self.event

	class Meta:
		ordering = ['event']

