# Generated by Django 2.2.8 on 2020-10-28 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201028_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
