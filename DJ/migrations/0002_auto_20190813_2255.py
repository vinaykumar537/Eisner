# Generated by Django 2.2.4 on 2019-08-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJ', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maptable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regulation', models.CharField(max_length=50)),
                ('businessdefinition_a', models.TextField()),
                ('process', models.CharField(max_length=50)),
                ('controlarea', models.CharField(max_length=50)),
                ('risk', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='FinalTable',
        ),
    ]
