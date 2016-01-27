from django.db import models
from hashlib import sha1
import string
import random
from Location.models import parish
from engineer.models import engineer


def slug_generator(size=4, chars=string.lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class housing(models.Model):
    id_o= models.BigIntegerField()
    name= models.CharField(max_length=300)
    parish= models.ForeignKey(parish)
    housing= models.IntegerField()
    description = models.CharField(max_length=300)
    engineer= models.ForeignKey(engineer)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_generator() + sha1(str(self.id)).hexdigest()[:4] + slug_generator()
        super(housing, self).save(*args, **kwargs)

    class Meta:
        db_table = 'housing'
        """permissions = (
            ('View_engineer', 'View incident'),
        )"""

    def __unicode__(self):
        return "%s - %s - %s" % (self.name, self.parish, self.id_o)