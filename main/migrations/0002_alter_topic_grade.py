# Generated by Django 4.1 on 2022-10-16 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='grade',
            field=models.ForeignKey(default='SS1', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.grade'),
        ),
    ]