# Generated by Django 3.1.3 on 2020-11-14 18:50

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
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('level', models.IntegerField()),
                ('abilityType', models.CharField(choices=[('Arcane Spell', 'Arcane Spell'), ('Divine Spell', 'Divine Spell'), ('Feat', 'Feat')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField(default=1)),
                ('abilities', models.ManyToManyField(blank=True, to='api.Ability')),
                ('characterClass', models.ManyToManyField(to='api.CharacterClass')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AbilityUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ability')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.character')),
            ],
        ),
    ]
