from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Creature, Ally, Enemy
from django.http import HttpResponse
from django.template import loader
from .forms import enemyForm


# Create your views here.
def Enemies(request):
    enemies = list(Enemy.objects.order_by("-date_modified"))

    
    template = loader.get_template("codex/enemies.html")
    form = enemyForm()
    if request.method == "POST":
        form = enemyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = enemyForm()

        context = {
        "enemies" : enemies,
        "form" : form,
        }
    return HttpResponse(template.render(context, request))

def Allies(request):
    allies = list(Ally.objects.order_by("-date_modified"))

    context = {
        "allies" : allies
    }
    template = loader.get_template("codex/allies.html")

    return HttpResponse(template.render(context, request))

def Creatures(request):
    creatures = list(Creature.objects.order_by("-date_modified"))

    context = {
        "creatures" : creatures
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