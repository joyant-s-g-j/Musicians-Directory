# Generated by Django 5.0.7 on 2024-09-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('fst_name', models.CharField(max_length=50)),
                ('lst_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=12)),
                ('insturment', models.CharField(max_length=50)),
            ],
        ),
    ]
