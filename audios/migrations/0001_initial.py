# Generated by Django 4.1.13 on 2023-12-14 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shiekh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('shiekh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audios.shiekh')),
            ],
        ),
        migrations.CreateModel(
            name='AudioEpisode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('audio_file', models.FileField(upload_to='audios/')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audios.book')),
            ],
        ),
    ]
