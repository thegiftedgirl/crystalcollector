# Generated by Django 3.0.4 on 2020-04-11 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleansing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cleanse', models.CharField(choices=[('H', 'HELD'), ('S', 'SUNLIGHT'), ('D', 'MOONLIGHT')], default='H', max_length=1)),
                ('crystal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Crystal')),
            ],
        ),
    ]
