# Generated by Django 4.2 on 2023-04-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'staff'), (1, 'admin')], default=1, max_length=50),
        ),
    ]