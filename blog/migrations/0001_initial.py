# Generated by Django 4.2.16 on 2024-10-22 04:08

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_satu', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('content_satu', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('image_dua', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('content_dua', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('image_tiga', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('content_tiga', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
