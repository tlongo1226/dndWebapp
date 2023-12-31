from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Creature, Ally, Enemy, JournalEntry
from django.http import HttpResponse
from django.template import loader
from .forms import enemyForm, AllyForm, CreatureForm, JournalForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import AllySerializer
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
def Enemies(request):
    enemies = list(Enemy.objects.order_by("-date_modified"))
    form = enemyForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('creatures')
    context = {
        "creatures" : enemies,
        "form" : form
    }
    template = loader.get_template("codex/creatures.html")
    return HttpResponse(template.render(context, request))

def Allies(request):
    allies = list(Ally.objects.order_by("-date_modified"))
    form = AllyForm(request.POST or None)

    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('allies')
    context = {
        "allies" : allies,
        "form" : form
    }
    template = loader.get_template("codex/allies.html")
    return HttpResponse(template.render(context, request))

def Creatures(request):
    creatures = list(Creature.objects.order_by("-date_modified"))
    form = CreatureForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('creatures')
    context = {
        "creatures" : creatures,
        "form" : form
    }
    template = loader.get_template("codex/creatures.html")
    return HttpResponse(template.render(context, request))

def index(request):
    mostRecentAlly = Ally.objects.order_by("-date_modified")[:1]
    mostRecentEnemy = Enemy.objects.order_by("-date_modified")[:1]
    allyResponse = "Most Recent Ally: "+ mostRecentAlly[0].name
    enemyResponse = "Most Recent Enemy: "+ mostRecentEnemy[0].name
    print(allyResponse + " " + enemyResponse)
    template = loader.get_template("codex/index.html")
    context = {
        "allyResponse" : allyResponse,
        "enemyResponse" : enemyResponse,
    } 
    return HttpResponse(template.render(context, request))

def enemyDetail(request, enemyID):
    enemy = get_object_or_404(Enemy, id= enemyID)
    return render(request, "codex/enemy_detail.html", {"enemy":enemy})

def AllyDetail(request, allyID):
    ally = get_object_or_404(Ally, id= allyID)
    return render(request, "codex/ally_detail.html", {"ally":ally})

def CreatureDetail(request, creatureID):
    creature = get_object_or_404(Creature, id = creatureID)
    return render(request, "codex/creature_detail.html", {"creature": creature})

def JournalEntriesView(request):
    entries = list(JournalEntry.objects.order_by("-date"))
    form = JournalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('journal_entries')

    context = {
        "entries" : entries,
        "form" : form
    }
    template = loader.get_template("codex/journal_entries.html")
    return HttpResponse(template.render(context, request))


class AllyView(viewsets.ModelViewSet):
    serializer_class = AllySerializer
    queryset = Ally.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    
    def get(self, request, *args, **kwargs):
        allies = Ally.objects.all()
        serializer = AllySerializer(allies, many = True)
        return Response(serializer.data)
    