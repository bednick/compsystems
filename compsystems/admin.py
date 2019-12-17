from django.contrib import admin
from django import forms
from django.db import models
from compsystems.models import *


class HierarchicalModelForm(forms.ModelForm):
    class Meta:
        model = HierarchicalModel
        fields = ['parent', 'name', 'context', ]


class HierarchicalModelAdmin(admin.ModelAdmin):
    form = HierarchicalModelForm
    list_display = ('id', 'name', 'parent', 'context')
    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size': '128'})},
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 8, 'cols': 128})},
    }


admin.site.register(HierarchicalModel, HierarchicalModelAdmin)

