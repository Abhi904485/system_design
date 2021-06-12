# Generated by Django 3.1.7 on 2021-06-12 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='name', max_length=500, verbose_name='name')),
                ('java', models.TextField(db_column='java', max_length=5000, verbose_name='java')),
                ('python', models.TextField(db_column='python', max_length=5000, verbose_name='python')),
                ('problem', models.ForeignKey(db_column='problem', on_delete=django.db.models.deletion.CASCADE, related_name='Codes', related_query_name='Code', to='problem.problem', verbose_name='problem')),
            ],
            options={
                'verbose_name': 'Codes',
                'verbose_name_plural': 'Codes',
                'db_table': 'codes',
            },
        ),
    ]
