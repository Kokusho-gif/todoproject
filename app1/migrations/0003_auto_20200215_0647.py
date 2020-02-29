# Generated by Django 3.0.3 on 2020-02-15 06:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200214_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('info', 'normal'), ('success', 'low')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]