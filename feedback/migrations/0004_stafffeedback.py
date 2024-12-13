# Generated by Django 5.1.3 on 2024-12-12 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('feedback', '0003_rename_content_doctorfeedback_reviews_and_more'),
        ('patients', '0004_alter_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_object_id', models.PositiveIntegerField()),
                ('reviews', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_feedback', to='patients.patient')),
                ('staff_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]