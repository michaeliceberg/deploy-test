# Generated by Django 4.0 on 2022-03-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first', '0002_delete_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ToDo', models.IntegerField()),
                ('Done', models.IntegerField()),
                ('Contrag', models.CharField(max_length=1000)),
            ],
        ),
    ]