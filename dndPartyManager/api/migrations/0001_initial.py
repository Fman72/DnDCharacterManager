# Generated by Django 3.1.3 on 2020-11-20 17:39

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
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('range', models.CharField(max_length=200, null=True)),
                ('components', models.CharField(max_length=200, null=True)),
                ('ritual', models.BooleanField(default=False)),
                ('duration', models.CharField(max_length=200, null=True)),
                ('concentration', models.BooleanField(default=False)),
                ('castingTime', models.CharField(max_length=200, null=True)),
                ('level', models.IntegerField()),
                ('school', models.CharField(max_length=200, null=True)),
                ('spellClass', models.CharField(max_length=200, null=True)),
                ('abilityType', models.CharField(choices=[('Arcane Spell', 'Arcane Spell'), ('Divine Spell', 'Divine Spell'), ('Feat', 'Feat')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField(default=1)),
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
            name='GameSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, null=True)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('historic', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LearnedAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uses', models.IntegerField()),
                ('learnedType', models.CharField(choices=[('Wizard Spell', 'Wizard Spell'), ('Sorcerer Spell', 'Sorcerer Spell'), ('Cleric Spell', 'Cleric Spell'), ('Feat', 'Feat')], max_length=100)),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ability')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='characterClass',
            field=models.ManyToManyField(to='api.CharacterClass'),
        ),
        migrations.AddField(
            model_name='character',
            name='currentSession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.gamesession'),
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
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
