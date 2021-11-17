# Generated by Django 3.2.9 on 2021-11-17 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('genre', models.CharField(choices=[('Adventure', 'Adventure'), ('Action', 'Action'), ('Puzzle', 'Puzzle'), ('FPS', 'FPS'), ('RPG', 'RPG'), ('Fighting Game', 'Fighting Game'), ('RTS', 'RTS'), ('Grand Strategy', 'Grand Strategy'), ('JRPG', 'JRPG'), ('Roguelike', 'Roguelike'), ('MMO', 'MMO'), ('TPS', 'TPS'), ('Shmup', 'Shmup'), ('Casual', 'Casual'), ('Party', 'Party')], max_length=128, null=True)),
                ('platform', models.CharField(choices=[('PC', 'PC'), ('NES', 'NES'), ('SNES', 'SNES'), ('Game Boy', 'Game Boy'), ('PSX', 'PSX'), ('N64', 'N64'), ('GBA', 'GBA'), ('GameCube', 'GameCube'), ('PS2', 'PS2'), ('XBOX', 'XBOX'), ('Wii', 'Wii'), ('PS3', 'PS3'), ('XBOX 360', 'XBOX 360'), ('DS', 'DS'), ('PSP', 'PSP'), ('Wii U', 'Wii U'), ('PS4', 'PS4'), ('XBOX One', 'XBOX One'), ('3DS', '3DS'), ('PS Vita', 'PS Vita'), ('Switch', 'Switch'), ('PS5', 'PS5'), ('XBOX Series X', 'XBOX Series X')], max_length=128, null=True)),
                ('release_date', models.DateField(null=True)),
                ('score', models.FloatField(default=0, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('comments', models.CharField(max_length=1024, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
