# Generated by Django 3.2 on 2022-07-28 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schSocialMedia', '0007_auto_20220726_0920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': '房间管理', 'verbose_name_plural': '房间管理'},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='content',
            new_name='descripton',
        ),
        migrations.RemoveField(
            model_name='room',
            name='commentcount',
        ),
        migrations.RemoveField(
            model_name='room',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='room',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='room',
            name='readcount',
        ),
        migrations.RemoveField(
            model_name='room',
            name='updated',
        ),
    ]
