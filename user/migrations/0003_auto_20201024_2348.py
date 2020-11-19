# Generated by Django 2.2.15 on 2020-10-24 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20200901_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0)),
                ('answer_text', models.TextField(blank=True, null=True)),
                ('time_post', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_heading', models.CharField(max_length=200)),
                ('question_text', models.TextField(blank=True, null=True)),
                ('vote', models.IntegerField(default=0)),
                ('time_post', models.DateTimeField(auto_now_add=True)),
                ('user_posted', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='followering',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='questions',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Voteofques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voteofans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user_posted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
