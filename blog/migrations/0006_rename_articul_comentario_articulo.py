# Generated by Django 5.1.7 on 2025-04-02 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comentario_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='articul',
            new_name='articulo',
        ),
    ]
