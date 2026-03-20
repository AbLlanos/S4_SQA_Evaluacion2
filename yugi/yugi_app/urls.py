from django.urls import path
from .views import *

# Poner nombre desde viewsa.py al mimsmo nivel

urlpatterns = [
    path('', cards, name='cards'),
    path('cards/<int:card_id>/', card_details, name='card_details'),
]
