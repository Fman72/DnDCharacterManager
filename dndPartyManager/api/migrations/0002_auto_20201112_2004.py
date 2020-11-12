# Generated by Django 3.1.3 on 2020-11-12 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userAuth', '0001_initial'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAuth.user'),
        ),
        migrations.AddField(
            model_name='abilityuse',
            name='ability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ability'),
        ),
        migrations.AddField(
            model_name='abilityuse',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.character'),
        ),
    ]