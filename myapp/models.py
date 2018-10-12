from django.db import models

class MyModel(models.Model):

	data = models.IntegerField()

	class Meta:
		permissions = (
			('can_hear', 'Can hear MyModel'),
		)
