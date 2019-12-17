from django.urls import path

from compsystems import views

app_name = 'compsystems'

urlpatterns = [
    path('models', views.models, name='models'),
]
