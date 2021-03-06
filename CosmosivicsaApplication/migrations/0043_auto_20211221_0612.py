# Generated by Django 3.2 on 2021-12-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosmosivicsaApplication', '0042_business_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Others_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=500)),
                ('office_name', models.CharField(max_length=1000)),
                ('message', models.TextField()),
                ('message_file', models.FileField(upload_to='home/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='business_contact',
            name='office_name',
        ),
    ]
