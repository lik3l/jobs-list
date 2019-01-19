from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Job(models.Model):
    TODO = 0
    IN_WORK = 1
    DONE = 2
    STATUSES = (
        (TODO, 'To do'),
        (IN_WORK, 'In progress'),
        (DONE, 'Done'),
    )

    created = models.DateTimeField(auto_now_add=True)
    ends = models.DateField(default=timezone.now)
    status = models.IntegerField(choices=STATUSES, default=TODO)
    name = models.CharField(max_length=255)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    client = models.ForeignKey(Company, on_delete=models.PROTECT)
    worker = models.ForeignKey('core.User', on_delete=models.PROTECT)
    rate = models.FloatField()
    payment = models.FloatField(default=0)
    qty = models.IntegerField(default=1)
    price = models.FloatField()

    def __str__(self):
        return self.name
