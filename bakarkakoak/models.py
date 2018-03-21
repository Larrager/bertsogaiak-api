from django.db import models
from django.template.defaultfilters import truncatechars
import uuid

class Bakarkakoa(models.Model):
    TYPES = (
        ('gaia', 'Gaia'),
        ('puntu-erantzuna', 'Puntu erantzuna'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField('Mota', max_length=20, choices=TYPES)
    text = models.TextField('Testua')
    created_at = models.DateTimeField('Sortua', auto_now_add=True)
    updated_at = models.DateTimeField('Aldatua', auto_now=True)

    @property
    def testu_laburra(self):
        return truncatechars(self.text, 80)

    def __str__(self):
        return self.text[:30]

    class Meta:
        verbose_name_plural = 'bakarkakoak'
