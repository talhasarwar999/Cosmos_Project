# Generated by Django 3.2 on 2021-12-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosmosivicsaApplication', '0037_auto_20211220_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our_Offices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/images')),
                ('address', models.CharField(max_length=350)),
                ('location', models.URLField(max_length=1000)),
                ('countryname', models.ManyToManyField(blank=True, to='CosmosivicsaApplication.CountryName')),
            ],
        ),
    ]
