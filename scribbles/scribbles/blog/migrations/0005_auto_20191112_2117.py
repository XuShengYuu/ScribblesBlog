# Generated by Django 2.1.3 on 2019-11-12 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_is_md'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id'], 'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
    ]
