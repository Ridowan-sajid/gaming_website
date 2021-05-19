from django.db import models
import datetime

class Game(models.Model):
    TYPE = (
        ('Offline', 'Offline'),
        ('Online', 'Online'),
        ('Offline & Online', 'Offline & Online'),
    )

    title=models.CharField(max_length=120)
    details=models.TextField(blank=False,null=False)
    type=models.CharField(max_length=20,choices=TYPE)
    time = datetime.datetime.now()
    feature_photo=models.ImageField(default="default.jpg",upload_to="images")

    def __str__(self):
        return self.title

class GameImage(models.Model):
    game = models.ForeignKey(Game, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.game.title




