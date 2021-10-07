# Generated by Django 3.2.5 on 2021-07-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolboxapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=250)),
                ('deadline', models.DateField()),
            ],
        ),
    ]
