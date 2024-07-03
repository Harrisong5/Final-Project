# Generated by Django 5.0.6 on 2024-07-03 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_joincomm'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sub',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='timestamp',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_id',
            new_name='postID',
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='community',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_comm', to='forum.community'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='imgLink',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='youtubeLink',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
