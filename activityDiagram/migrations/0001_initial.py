# Generated by Django 3.1.7 on 2021-06-12 11:50

import SystemDesign.utility
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityDiagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.TextField(db_column='activity', max_length=5000, verbose_name='activity')),
                ('image', SystemDesign.utility.SVGAndImageField(upload_to='activityDiagram', verbose_name='image')),
                ('problem', models.ForeignKey(db_column='problem', on_delete=django.db.models.deletion.CASCADE, related_name='ActivityDiagrams', related_query_name='ActivityDiagram', to='problem.problem', verbose_name='problem')),
            ],
            options={
                'verbose_name': 'ActivityDiagram',
                'verbose_name_plural': 'ActivityDiagrams',
                'db_table': 'activity',
            },
        ),
    ]
