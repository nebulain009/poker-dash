from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Player)
admin.site.register(models.Tournament)
admin.site.register(models.Match)
admin.site.register(models.PlayerMatchResult)
admin.site.register(models.Round)
admin.site.register(models.Hand)
admin.site.register(models.PlayerRoundResult)
admin.site.register(models.ResultType)
