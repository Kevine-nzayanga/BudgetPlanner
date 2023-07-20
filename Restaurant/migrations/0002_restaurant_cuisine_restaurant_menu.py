# Generated by Django 4.2.3 on 2023-07-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(choices=[('american', 'American'), ('chinese', 'Chinese'), ('italian', 'Italian'), ('mexican', 'Mexican'), ('indian', 'Indian')], default='chinese', max_length=20),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu',
            field=models.TextField(blank=True, null=True),
        ),
    ]
