from django.db import models
from django.template.defaultfilters import truncatechars
import uuid

class Ofizioa(models.Model):
    METRICS = (
        ('zortziko txikia', 'Zortziko txikia'),
        ('zortziko handia', 'Zortziko handia'),
        ('hamarreko txikia', 'Hamarreko txikia'),
        ('hamarreko handia', 'Hamarreko handia'),
        ('kopla', 'Kopla'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    metric = models.CharField('Neurria', max_length=20, choices=METRICS)
    text = models.TextField('Testua')
    created_at = models.DateTimeField('Sortua', auto_now_add=True)
    updated_at = models.DateTimeField('Aldatua', auto_now=True)

    @property
    def testu_laburra(self):
        return truncatechars(self.text, 80)

    def __str__(self):
        return self.text[:30]

    class Meta:
        verbose_name_plural = 'ofizioak'
