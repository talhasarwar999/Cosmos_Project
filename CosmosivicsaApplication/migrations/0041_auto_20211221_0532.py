# Generated by Django 3.2 on 2021-12-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosmosivicsaApplication', '0040_academic_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=500)),
                ('job_title', models.CharField(max_length=1000)),
                ('office_name', models.CharField(max_length=1000)),
                ('url', models.URLField(max_length=1000)),
                ('message', models.TextField()),
                ('message_file', models.FileField(null=True, upload_to='home/images')),
            ],
        ),
        migrations.AlterField(
            model_name='academic_contact',
            name='message_file',
            field=models.FileField(null=True, upload_to='home/images'),
        ),
        migrations.AlterField(
            model_name='press_contact',
            name='message_file',
            field=models.FileField(upload_to='home/images'),
        ),
    ]
