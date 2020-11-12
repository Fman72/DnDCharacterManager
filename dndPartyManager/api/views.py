from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.core import serializers
from .utility import queryDictToDict
from .models import Ability, Character, AbilityUse, CharacterClass

# Create your views here.


def index(request):
    return HttpResponse("This is the API index.")

# This is the default behaviour for an endpoint.
# Query the DB with get params.
# Will add auth later.
# Creating individual views lets me extend them later to handle un expected use cases. I can remain flexible.
class ModelView(View):
    viewClass = None
    
    def get(self, request):
        requestParams = queryDictToDict(request.GET)
        if id:
            model = self.viewClass.objects.filter(**requestParams)
            data = serializers.serialize('json', model)
            response = HttpResponse(content_type='application/json', content=data)
            return response

class AbilityView(ModelView):
    viewClass = Ability

# TODO: Need to prevent users accessing anyones characters
class CharacterView(ModelView):
    viewClass = Character

class AbilityUseView(ModelView):
    viewClass = AbilityUse

class CharacterClassView(ModelView):
    viewClass = CharacterClass