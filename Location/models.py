from django.db import models
from engineer.models import slug_generator
from hashlib import sha1
import string
import random


class municipality(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_generator() + sha1(str(self.id)).hexdigest()[:4] + slug_generator()
        super(municipality, self).save(*args, **kwargs)

    class Meta:
        db_table = 'municipality'
        """permissions = (
            ('View_engineer', 'View incident'),
        )"""

    def __unicode__(self):
        return "%s" % (self.name)


class parish(models.Model):
    name = models.CharField(max_length=300)
    municipality = models.ForeignKey(municipality)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_generator() + sha1(str(self.id)).hexdigest()[:4] + slug_generator()
        super(parish, self).save(*args, **kwargs)

    class Meta:
        db_table = 'parish'
        """permissions = (
            ('View_engineer', 'View incident'),
        )"""

    def __unicode__(self):
        return "%s - %s " % (self.name, self.municipality)


class sector(models.Model):
    name = models.CharField(max_length=300)
    parish = models.ForeignKey(parish)
    slug = models.SlugField()
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_generator() + sha1(str(self.id)).hexdigest()[:4] + slug_generator()
        super(sector, self).save(*args, **kwargs)

    class Meta:
        db_table = 'sector'
        """permissions = (
            ('View_engineer', 'View incident'),
        )"""

    def __unicode__(self):
        return "%s - %s " % (self.name, self.parish)