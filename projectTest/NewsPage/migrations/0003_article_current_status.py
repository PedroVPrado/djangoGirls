# Generated by Django 2.2.5 on 2019-10-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPage', '0002_auto_20190930_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='current_status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISH', 'Publish'), ('ARCHIVE', 'Archive')], default='DRAFT', max_length=7),
        ),
    ]