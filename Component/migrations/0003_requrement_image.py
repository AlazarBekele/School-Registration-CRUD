# Generated by Django 5.1.3 on 2024-11-08 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Component', '0002_alter_departement_discribe_alter_requrement_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='requrement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
