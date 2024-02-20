from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class State(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=200, verbose_name=_("Qisqa nomi [attr]"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Xolat')
        verbose_name_plural = _('Xolatlar')
        db_table = 'state'
