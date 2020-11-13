from django.urls import path, include
from rest_framework import routers
from . import viewSets


router = routers.DefaultRouter()
router.register(r'characters', viewSets.CharacterViewSet)
router.register(r'abilities', viewSets.AbilityViewSet)
router.register(r'character_classes', viewSets.CharacterClassViewSet)
router.register(r'ability_uses', viewSets.AbilityUseViewSet)

urlpatterns = [
    path('', include(router.urls))
]