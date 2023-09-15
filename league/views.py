from django.shortcuts import render
from .models import Player
from django.db.models import Sum, Case, IntegerField, When, F

# Create your views here.
def Home(request):
    players = Player.objects.annotate(
        total_earnings=Sum('playermatchresult__money_result'),
        total_tournament_wins=Sum(
            Case(
                When(playertournamentresult__result__name='Win', then=1),
                default=0,
                output_field=IntegerField(),
            ),
            distinct=True,
        ),
        total_match_wins=Sum(
            Case(
                When(playermatchresult__result__name='Win', then=1),
                default=0,
                output_field=IntegerField(),
            ),
        )
    ).order_by('-total_earnings')

    context = {
        "players": players,
    }
    return render(request, 'league/index.html', context)

def Hands(request):
    return render(request, 'league/hands.html')