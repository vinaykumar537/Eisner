# Generated by Django 2.1.12 on 2019-09-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJ', '0018_auto_20190926_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.TextField()),
                ('BusinessActivity', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='bareg',
            name='category',
            field=models.TextField(default='Individual'),
        ),
        migrations.AlterField(
            model_name='controlreg',
            name='category',
            field=models.TextField(default='Individual'),
        ),
        migrations.AlterField(
            model_name='processreg',
            name='category',
            field=models.TextField(default='Individual'),
        ),
        migrations.AlterField(
            model_name='riskreg',
            name='category',
            field=models.TextField(default='Individual'),
        ),
    ]
