# Generated by Django 4.1.2 on 2022-10-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('albumId', models.IntegerField()),
                ('url', models.URLField()),
            ],
        ),
    ]