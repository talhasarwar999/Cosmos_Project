# Generated by Django 3.2 on 2021-12-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosmosivicsaApplication', '0044_remove_others_contact_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career_contact',
            name='office_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='others_contact',
            name='office_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
