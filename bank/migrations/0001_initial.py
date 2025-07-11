# Generated by Django 5.2.4 on 2025-07-05 15:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(max_length=5)),
                ('quantity', models.IntegerField()),
                ('donation_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('blood_type', models.CharField(max_length=5)),
                ('contact_info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_date', models.DateField(auto_now_add=True)),
                ('blood_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bloodunit')),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.donor')),
            ],
        ),
        migrations.AddField(
            model_name='bloodunit',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.donor'),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('blood_type', models.CharField(max_length=5)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Transfusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfusion_date', models.DateField(auto_now_add=True)),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountant_transfusions', to=settings.AUTH_USER_MODEL)),
                ('blood_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bloodunit')),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.patient')),
                ('receptionist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptionist_transfusions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
