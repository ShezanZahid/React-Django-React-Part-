# Generated by Django 3.0.8 on 2021-08-30 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postType', '0001_initial'),
        ('tasks', '0003_task_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='post_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='postType.PostType'),
        ),
    ]
