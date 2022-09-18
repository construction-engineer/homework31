# Generated by Django 4.0.5 on 2022-07-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ads/'),
        ),
    ]
