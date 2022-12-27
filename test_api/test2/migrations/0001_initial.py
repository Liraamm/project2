# Generated by Django 4.1.4 on 2022-12-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('commentary', models.CharField(max_length=40)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
