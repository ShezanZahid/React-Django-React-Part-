# Generated by Django 3.2.7 on 2021-09-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postType', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttype',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
