# Generated by Django 4.1 on 2022-10-16 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_topic_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.grade'),
        ),
    ]