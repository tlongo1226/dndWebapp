from django.urls import path
from . import views

urlpatterns = [
    path("enemies/", views.Enemies, name="Enemies"),
    path("allies/", views.Allies, name="Allies"),
    path("creatures/", views.Creatures, name="Creatures"),
    path("index/", views.index, name="index"),
    path("enemy_detail/<int:enemyID>/", views.enemyDetail, name="enemy_detail"),
    path('api/journal-entries/', views.journal_entries, name='journal-entries'),
]