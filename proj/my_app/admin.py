from django.contrib import admin
from my_app import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Project)
admin.site.register(models.ProjectDetail)
admin.site.register(models.PostToProject)
admin.site.register(models.ProjectComment)


