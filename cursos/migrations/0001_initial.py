# Generated by Django 5.1.7 on 2025-03-28 02:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblCategoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_nombre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tbl_categoria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblCurso',
            fields=[
                ('curso_id', models.AutoField(primary_key=True, serialize=False)),
                ('curso_titulo', models.CharField(max_length=255)),
                ('curso_descripcion', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.tblcategoria')),
            ],
            options={
                'db_table': 'tbl_curso',
                'managed': True,
            },
        ),
    ]
