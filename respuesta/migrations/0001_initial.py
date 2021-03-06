# Generated by Django 3.1.6 on 2021-02-17 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField(verbose_name='Respuesta otorgada')),
                ('fecha_respuesta', models.DateField(auto_now_add=True, verbose_name='Fecha de Respuesta')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.pregunta')),
                ('user', models.OneToOneField(default='17318072', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
