from django.db import models
from hashlib import sha1
import string
import random


def slug_generator(size=4, chars=string.lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class engineer(models.Model):
    name = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    ci = models.IntegerField(max_length=10)
    civ = models.IntegerField(max_length=10)
    email = models.CharField(max_length=300)
    phone = models.IntegerField(max_length=12)
    direction = models.TextField(max_length=500)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_generator() + sha1(str(self.id)).hexdigest()[:4] + slug_generator()
        super(engineer, self).save(*args, **kwargs)

    class Meta:
        db_table = 'engineer'
        """permissions = (
            ('View_engineer', 'View incident'),
        )"""

    def __unicode__(self):
        return "%s - %s - %s" % (self.name, self.ci, self.civ)