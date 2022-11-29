from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Tiptype(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Tip(models.Model):
    title = models.CharField(max_length=150)
    tiptype = models.ForeignKey('Tiptype', on_delete=models.SET_NULL, null=True)
    why_10 = models.TextField(max_length=600)
    more_information = models.TextField(max_length=600)
    tip_date = models.DateField(null=True, blank=True)
    tip_giver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['tip_date']

    def __str__(self):
        return f'{self.title} ({self.tiptype})'

    def get_absolute_url(self):
        return reverse("tip_detail", kwargs={"pk":self.pk})

