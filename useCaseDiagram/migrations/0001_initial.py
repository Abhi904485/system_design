# Generated by Django 3.1.7 on 2021-06-03 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UseCaseDiagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='usecases', verbose_name='image')),
                ('problem', models.ForeignKey(db_column='problem', on_delete=django.db.models.deletion.CASCADE, related_name='UseCaseDiagrams', related_query_name='UseCaseDiagram', to='problem.problem', verbose_name='problem')),
            ],
            options={
                'verbose_name': 'UseCaseDiagram',
                'verbose_name_plural': 'UseCaseDiagrams',
                'db_table': 'usecasediagram',
            },
        ),
        migrations.CreateModel(
            name='UseCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_case', models.CharField(db_column='use_case', max_length=5000, verbose_name='use_case')),
                ('usecasediagram', models.ForeignKey(db_column='usecasediagram', on_delete=django.db.models.deletion.CASCADE, related_name='usecase', related_query_name='usecase', to='useCaseDiagram.usecasediagram', verbose_name='usecases')),
            ],
            options={
                'verbose_name': 'UseCases',
                'verbose_name_plural': 'UseCases',
                'db_table': 'use_case',
            },
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(db_column='actor', max_length=5000, verbose_name='actor')),
                ('usecasediagram', models.ForeignKey(db_column='usecasediagram', on_delete=django.db.models.deletion.CASCADE, related_name='actors', related_query_name='actor', to='useCaseDiagram.usecasediagram', verbose_name='usecasediagram')),
            ],
            options={
                'verbose_name': 'Actors',
                'verbose_name_plural': 'Actors',
                'db_table': 'actor',
            },
        ),
    ]
