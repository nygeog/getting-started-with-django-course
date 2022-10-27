# Generated by Django 4.0.2 on 2022-04-28 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('birth_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.author')),
            ],
            options={
                'verbose_name': 'Bookington',
                'verbose_name_plural': 'Bookington McBookFace',
                'ordering': ['author__last_name', 'title'],
            },
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['title', 'author'], name='catalog_boo_title_5b6232_idx'),
        ),
    ]
