from django.db import models
from hashlib import sha1
import string
import random
from django.contrib.auth.models import User


def slug_generator(size=4, chars=string.lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class userP(models.Model):
    user= models.OneToOneField(User)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_generator() + sha1(str(self.id)).hexdigest()[:4] + slug_generator()
        super(userP, self).save(*args, **kwargs)

    class Meta:
        db_table = 'UserP'
        """permissions = (
            ('View_engineer', 'View incident'),
        )"""
    
    def __unicode__(self):
        return "%s" % (self.user )

