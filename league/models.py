from django.db import models

# Create your models here.

# Players Table
class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50, null=True, blank=True)
    join_date = models.DateField(auto_now_add=True, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# Tournaments Table
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    buy_in_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
# Matches Table
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match_date = models.DateField()
    blinds_level = models.CharField(max_length=50)

    def __str__(self):
        return str(self.match_date)
    
# Win, Lose, Fold
class ResultType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class PlayerTournamentResult(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    result = models.ForeignKey(ResultType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name} ({self.result} {self.tournament})"

# Player_Match_Results Table
class PlayerMatchResult(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    position = models.IntegerField()
    result = models.ForeignKey(ResultType, on_delete=models.CASCADE)
    money_result = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name} ({self.result} {self.match})"

class Round(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"Round {self.number} (Match {self.match})"
    
class Hand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PlayerRoundResult(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    result = models.ForeignKey(ResultType, on_delete=models.CASCADE)
    hand = models.ForeignKey(Hand, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name} ({self.result})"
    
