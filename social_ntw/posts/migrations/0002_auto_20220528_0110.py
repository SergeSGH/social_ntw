# Generated by Django 2.2.16 on 2022-05-27 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='isliked',
            options={'verbose_name': 'Лайк', 'verbose_name_plural': '  Лайки'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Пост', 'verbose_name_plural': ' Посты'},
        ),
    ]