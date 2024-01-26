from django.db import models
from uuslug import uuslug
import uuid


class SlugModelMixin(models.Model):
    slugged_field = ""

    slug = (
        models.SlugField(unique=True, default=str(uuid.uuid4()))
    )

    class Meta:
        abstract = True

    def prepare_slug(self):
        _slugged_field = getattr(self, self.slugged_field)
        self.slug = uuslug(_slugged_field, instance=self)

    def save(self, *args, **kwargs):
        self.prepare_slug()
        super(SlugModelMixin, self).save(*args, **kwargs)