# Generated by Django 2.2.1 on 2019-05-26 08:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pulse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Primitive', 'Primitive'), ('CORPSE', 'CORPSE'), ('Gaussian', 'Gaussian'), ('CinBB', 'CinBB'), ('CinSK', 'CinSK')], max_length=20)),
                ('max_rabi_rate', models.FloatField()),
                ('polar_angle', models.FloatField()),
            ],
        ),
    ]
