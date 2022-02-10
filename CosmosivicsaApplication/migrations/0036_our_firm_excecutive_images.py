# Generated by Django 3.2 on 2021-12-20 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CosmosivicsaApplication', '0035_our_firm_our_firmparagraphandimage_our_values_our_valuesparagraphandimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our_Firm_Excecutive_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/images')),
                ('firmimageFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firm_images', to='CosmosivicsaApplication.our_firm')),
            ],
        ),
    ]
