from django.utils import timezone
from django.db import models


class Game(models.Model):
    TYPE = (
        ('Offline', 'Offline'),
        ('Online', 'Online'),
        ('Offline & Online', 'Offline & Online'),
    )
    GENRE = (
        ('Action', 'Action'),
        ('Action-adventure', 'Action-adventure'),
        ('Adventure', 'Adventure'),
        ('Role-playing', 'Role-playing'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
        ('Simulation', 'Simulation'),
    )

    title = models.CharField(max_length=120)
    details = models.TextField(blank=False, null=False)
    type = models.CharField(max_length=20, choices=TYPE)
    genre = models.CharField(max_length=20, choices=GENRE)
    time = models.DateTimeField(default=timezone.now)
    feature_photo = models.ImageField(default="default.jpg", upload_to="images")
    images1 = models.ImageField(upload_to="images")
    images2 = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title


# class GameImage(models.Model):
#     game = models.ForeignKey(Game, default=None, on_delete=models.CASCADE)
#     images = models.ImageField(upload_to='images')
#
#     def __str__(self):
#         return self.game.title

class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    game_comment = models.CharField(max_length=200, null=False, blank=False)
    time = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    commenter = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.game.title
