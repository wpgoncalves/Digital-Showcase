# Generated by Django 4.0.4 on 2022-05-15 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_alter_stores_group_alter_stores_title_establishment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='title_establishment',
            field=models.CharField(max_length=27, unique=True, verbose_name='Fantasia'),
        ),
    ]
