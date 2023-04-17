# Generated by Django 4.2 on 2023-04-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('composition', models.TextField()),
                ('rate', models.FloatField()),
                ('created_data', models.DateField(auto_now=True)),
                ('modified_data', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
