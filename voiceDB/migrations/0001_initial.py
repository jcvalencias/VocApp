# Generated by Django 4.1.4 on 2023-09-06 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VocabDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('French', models.TextField()),
                ('Spanish', models.TextField()),
                ('Example', models.TextField()),
                ('learning_rate', models.FloatField()),
                ('audio_file', models.FileField(upload_to='audio_files/')),
            ],
        ),
    ]