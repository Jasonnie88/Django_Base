# Generated by Django 3.2 on 2022-07-26 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schSocialMedia', '0006_auto_20220726_0137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-pub_date'], 'verbose_name': '房间管理', 'verbose_name_plural': '房间管理'},
        ),
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='主持人'),
        ),
        migrations.AlterField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schSocialMedia.topic', verbose_name='主题'),
        ),
    ]