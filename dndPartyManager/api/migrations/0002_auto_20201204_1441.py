# Generated by Django 3.1.3 on 2020-12-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='abilityuse',
            index=models.Index(fields=['targetId', 'targetType'], name='api_ability_targetI_7966d1_idx'),
        ),
        migrations.AddIndex(
            model_name='abilityuse',
            index=models.Index(fields=['casterId', 'casterType'], name='api_ability_casterI_5f336c_idx'),
        ),
    ]
