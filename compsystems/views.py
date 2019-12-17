from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from compsystems.models import HierarchicalModel


def models(request: WSGIRequest):
    model_id = request.GET.get('model_id')
    search = request.GET.get('search')

    objects = HierarchicalModel.objects.all()
    context_objs = []
    if model_id:
        try:
            context_objs = [HierarchicalModel.objects.get(id=model_id),]
        except:
            pass
    elif search:
        try:
            context_objs = HierarchicalModel.objects.filter(context__contains=search)
        except Exception:
            pass
    return render(request, 'base.html', {'models': objects, 'context_objs': context_objs})
