from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
	no_telp = models.CharField(max_length = 31, null= True, blank=False)
	tanggal_lahir = models.DateField(null= True, blank=False)
	email = models.EmailField(_('email address'), unique=True)
	username = models.CharField(max_length = 31, null=False, blank=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']