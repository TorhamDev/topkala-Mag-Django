# Generated by Django 3.2.9 on 2021-11-14 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('slug', models.SlugField()),
                ('title_photo', models.ImageField(upload_to='./web/static/uploads/articles_photo')),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'article',
            },
        ),
        migrations.CreateModel(
            name='Athoder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='./web/static/uploads/articles_photo')),
                ('name', models.CharField(max_length=80)),
                ('info', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('comment_email', models.EmailField(max_length=254)),
                ('article_commetns', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.articles')),
            ],
            options={
                'verbose_name': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'tag',
            },
        ),
        migrations.CreateModel(
            name='Repaly_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('replay_email', models.EmailField(max_length=254)),
                ('repaly', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.comments')),
            ],
            options={
                'verbose_name': 'Repaly_comment',
            },
        ),
        migrations.CreateModel(
            name='My_selected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles_selected', models.ManyToManyField(to='web.Articles')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='Tags',
            field=models.ManyToManyField(help_text='?????? ?????? ???????? ?????????? ?????????????? ?????????? ????????<br>', to='web.Tags', verbose_name='tag'),
        ),
        migrations.AddField(
            model_name='articles',
            name='athoder_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.athoder', verbose_name='Athoder name'),
        ),
        migrations.AddField(
            model_name='articles',
            name='category_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.category'),
        ),
    ]
