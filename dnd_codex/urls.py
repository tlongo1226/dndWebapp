from django.urls import path
from . import views

urlpatterns = [
    path("enemies/", views.Enemies, name="Enemies"),
    path("allies/", views.Allies, name="allies"),
    path("creatures/", views.Creatures, name="Creatures"),
    path("index/", views.index, name="index"),
    path("enemy_detail/<int:enemyID>/", views.enemyDetail, name="enemy_detail"),
    path("ally_detail/<int:allyID>/", views.AllyDetail, name="ally_detail"),
    path("creature_detail/<int:creatureID>/", views.CreatureDetail, name="creature_detail"),

]