from django.db import models
from django.forms import forms

class GameForm(forms.Form):
    game_comment = models.CharField()
