# Generated by Django 4.1.2 on 2022-11-13 18:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_servs_servicio_detalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='servs',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]