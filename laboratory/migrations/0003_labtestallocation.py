# Generated by Django 5.1.3 on 2024-12-09 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0002_alter_laboratory_user'),
        ('medical_records', '0005_labprescription_test_instructions_and_more'),
        ('patients', '0004_alter_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTestAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocated_on', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('allocated', 'Allocated'), ('completed', 'Completed')], default='allocated', max_length=20)),
                ('laboratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_test_allocations', to='laboratory.laboratory')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_tests', to='patients.patient')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='medical_records.labprescription')),
            ],
        ),
    ]
