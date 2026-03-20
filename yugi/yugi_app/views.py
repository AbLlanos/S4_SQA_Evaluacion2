from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Card

def cards(request):
    card_list = Card.objects.all().order_by('card_id')

    paginator   = Paginator(card_list, 4)
    page_number = request.GET.get('page')
    cards_page  = paginator.get_page(page_number)

    return render(request, 'cards/cards.html', {'cards': cards_page})


def card_details(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/cards_details.html', {'card': card})


