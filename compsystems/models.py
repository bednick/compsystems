from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    'HierarchicalModel',
]


class HierarchicalModel(models.Model):
    class Meta:
        verbose_name = _('hierarchical model')
        verbose_name_plural = _('hierarchical models')

    parent = models.ForeignKey('HierarchicalModel', parent_link=True, related_name='children',
                               on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(_('name'), max_length=1024, unique=True, null=False)
    context = models.TextField(_('context'), max_length=10000, null=False)

    def __str__(self):
        if len(self.context) >= 10:
            return f'{self.id}. {self.name}: {self.context[:10]}...'
        else:
            return f'{self.id}. {self.name}: {self.context}'
