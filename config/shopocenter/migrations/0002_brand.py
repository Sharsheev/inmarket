# Generated by Django 2.1 on 2018-08-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopocenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]