from django.db import models
from django.shortcuts import reverse


class Department(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('department_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('department_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('department_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta():
        ordering = ['title']
