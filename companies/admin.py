from django.contrib import admin
from companies import models

admin.site.register(models.CompanyRole)
admin.site.register(models.Company)
admin.site.register(models.Office)
