from django.db import models
from django.db.models import CASCADE


class Location(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

	class Meta:
		verbose_name = 'Локация'
		verbose_name_plural = 'Локации'

	def __str__(self):
		return self.name


class User(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=30)
	role = models.CharField(max_length=20)
	age = models.PositiveIntegerField()
	location = models.ForeignKey(Location, on_delete=CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

	def __str__(self):
		return self.username
