# Generated by Django 3.0.8 on 2021-08-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=100)),
                ('created_by', models.CharField(default='admin', max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
