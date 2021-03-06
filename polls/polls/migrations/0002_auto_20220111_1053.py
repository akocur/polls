# Generated by Django 2.2.10 on 2022-01-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.RemoveField(
            model_name='question',
            name='poll',
        ),
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.ManyToManyField(related_name='questions', to='polls.Poll'),
        ),
    ]
