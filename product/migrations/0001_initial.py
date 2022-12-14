# Generated by Django 3.2.9 on 2022-04-23 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('ordering', models.ImageField(default=0, upload_to='')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
    ]
