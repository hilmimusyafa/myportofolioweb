# Generated by Django 5.0.4 on 2024-05-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('imageorganization', models.ImageField(upload_to='')),
                ('organization', models.CharField(blank=True, max_length=120)),
                ('year', models.CharField(blank=True, max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
