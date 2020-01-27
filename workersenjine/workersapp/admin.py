from django.contrib import admin
from .model.department import Department
from .model.worker import Worker
admin.site.register(Worker)
admin.site.register(Department)