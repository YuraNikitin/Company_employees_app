from django.db import models
from time import time
from django.utils.text import slugify
from django.shortcuts import reverse
from ..model.department import Department


class Worker(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    surname = models.CharField(max_length=30, db_index=True)
    lastName = models.CharField(max_length=30, blank=True)
    dateBirth = models.DateTimeField()
    email = models.EmailField(max_length=150, unique=True, db_index=True)
    phone = models.CharField(max_length=15, db_index=True, unique=True)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(blank=True, null=True)
    position = models.CharField(max_length=35, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    department = models.ForeignKey(Department, related_name='workers', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('worker_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('worker_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('worker_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{},{}'.format(self.name, self.surname)

    class Meta():
        ordering = ['surname']


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))
