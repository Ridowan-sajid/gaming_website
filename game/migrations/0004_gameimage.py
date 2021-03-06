# Generated by Django 3.1.6 on 2021-05-19 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20210518_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images')),
                ('game', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]
