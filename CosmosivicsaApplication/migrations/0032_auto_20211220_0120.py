# Generated by Django 3.2 on 2021-12-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosmosivicsaApplication', '0031_alter_serviceparagraph_projectfk'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_apply',
            name='job_bus',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job_apply',
            name='job_cat',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job_apply',
            name='job_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
