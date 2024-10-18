# Generated by Django 4.2.16 on 2024-10-18 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sains', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tes',
            options={'verbose_name_plural': 'Tes'},
        ),
        migrations.CreateModel(
            name='ResultSains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sains.tes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
