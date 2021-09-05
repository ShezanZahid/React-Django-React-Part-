# Generated by Django 3.0.8 on 2021-08-31 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postType', '0001_initial'),
        ('tasks', '0004_auto_20210830_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.AddField(
            model_name='task',
            name='created_by',
            field=models.CharField(default='2021-08-31T08:06:03.212493Z', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='task',
            name='post_privacy',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='post_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_title', to='postType.PostType'),
        ),
    ]