from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


# Create your models here.


class Data(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	zignum = models.CharField(verbose_name=_('Scan baracode1'),max_length=255,null=True,blank=False)
	unitsn = models.CharField(verbose_name=_('Scan  baracode1'),max_length=12,null=True,blank=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)


	class Meta:
		verbose_name = _('Data')
		verbose_name_plural = _('Datas')
		ordering = ['-created'] #recent objects
