from django.contrib import admin
from django_api import models

admin.site.registry(models.UserProfile)
