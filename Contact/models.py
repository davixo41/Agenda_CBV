from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    alias = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.alias, self.phone)