# Generated by Django 4.2.8 on 2023-12-24 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audios', '0009_alter_shiekh_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/')),
            ],
        ),
    ]
