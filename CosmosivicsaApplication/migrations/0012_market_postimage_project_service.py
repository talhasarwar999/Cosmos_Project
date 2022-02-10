# Generated by Django 3.2 on 2021-12-17 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CosmosivicsaApplication', '0011_post_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketname', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicename', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('client', models.CharField(max_length=500)),
                ('include', models.CharField(max_length=900)),
                ('area', models.CharField(max_length=900)),
                ('cost', models.CharField(max_length=900)),
                ('status', models.CharField(max_length=800)),
                ('multipleimages', models.ImageField(upload_to='home/images')),
                ('countryname', models.ManyToManyField(to='CosmosivicsaApplication.CountryName')),
                ('marketname', models.ManyToManyField(to='CosmosivicsaApplication.Market')),
                ('servicename', models.ManyToManyField(to='CosmosivicsaApplication.Service')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='home/images')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CosmosivicsaApplication.project')),
            ],
        ),
    ]
