# Generated by Django 3.1.4 on 2021-08-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_doodledesign'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoodleBites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
