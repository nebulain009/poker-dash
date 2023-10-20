from django.shortcuts import render
from .models import Player
from django.db.models import Sum, Case, IntegerField, When, F

# Create your views here.
def Home(request):
    players = Player.objects.annotate(

        total_earnings = Sum(F('playermatchresult__money_result') - F('playermatchresult__match__buy_in_amount')),

        total_tournament_wins=Sum(
            Case(
                When(playertournamentresult__result__name='Win', then=1),
            ),
            distinct=True,
        ),
        total_match_wins=Sum(
            Case(
                When(playermatchresult__result__name='Win', then=1),
            ),
        ),
        total_points=Sum(
            Case(
                When(
                    playermatchresult__result__name='Win',
                    then=(F('playermatchresult__match__buy_in_amount') * 2 * ((F('playermatchresult__match__number_of_players') - 3) / 4 + 0.5)),
                ),
                default=0,
                output_field=IntegerField()
            )
        ) + F('total_earnings')
    ).order_by('-total_points')

    context = {
        "players": players,
    }
    return render(request, 'league/index.html', context)


def Hands(request):
    return render(request, 'league/hands.html')