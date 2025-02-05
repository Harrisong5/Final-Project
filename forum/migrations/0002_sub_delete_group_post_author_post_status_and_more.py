# Generated by Django 5.0.6 on 2024-07-03 10:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='forum_posts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
