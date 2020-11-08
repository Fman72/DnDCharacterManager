from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.ModelView.as_view()),
    path('ability', views.AbilityView.as_view()),
]