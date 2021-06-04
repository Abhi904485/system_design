# Generated by Django 3.1.7 on 2021-06-03 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classDiagram', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classdiagram',
            name='classes',
        ),
        migrations.AlterModelTable(
            name='classdiagram',
            table='classdiagram',
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=5000, verbose_name='name')),
                ('class_diagram', models.ForeignKey(db_column='Class', on_delete=django.db.models.deletion.CASCADE, related_name='Classes', related_query_name='Class', to='classDiagram.classdiagram', verbose_name='class Diagram')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Class',
                'db_table': 'class',
            },
        ),
    ]
