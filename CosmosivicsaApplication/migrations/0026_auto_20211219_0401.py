# Generated by Django 3.2 on 2021-12-19 12:01

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosmosivicsaApplication', '0025_alter_publish_job_requisition_vacancy_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publish_job',
            name='requirements',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='publish_job',
            name='requisition_vacancy_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='publish_job',
            name='responsibiltie',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]