from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.ModelView.as_view()),
    path('ability', views.AbilityView.as_view()),
    path('character', views.CharacterView.as_view()),
    path('character_class', views.CharacterClassView.as_view()),
    path('ability_use', views.AbilityUseView.as_view()),
]