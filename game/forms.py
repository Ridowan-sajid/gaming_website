from django import forms

class GameForm(forms.Form):
    game_comment = forms.CharField(max_length=200)
