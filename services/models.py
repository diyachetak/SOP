from django.db import models

# Create your models here.
class RCM_Services(models.Model):
	service_name =  models.TextField()

	def _str_(self):
		return self.service_name

