# Generated by Django 4.0.3 on 2022-03-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_no', models.IntegerField()),
                ('sign', models.ImageField(upload_to='')),
                ('Aaddhar_copy', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'attachments',
            },
        ),
        migrations.CreateModel(
            name='Complainant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_no', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('father_name', models.CharField(max_length=150)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('nationality', models.CharField(max_length=50)),
                ('relation_with_vicitm', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('addhar_no', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'complainant_info',
            },
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_no', models.IntegerField()),
                ('doa', models.DateField()),
                ('poo', models.TextField()),
                ('ooo_from', models.DateTimeField()),
                ('ooo_to', models.DateTimeField()),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'crime_info',
            },
        ),
        migrations.CreateModel(
            name='Fir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_no', models.IntegerField()),
                ('detail_info', models.TextField()),
            ],
            options={
                'db_table': 'fir_details',
            },
        ),
        migrations.CreateModel(
            name='FirModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_no', models.IntegerField()),
                ('crime_type', models.CharField(max_length=150)),
                ('fir_status', models.CharField(max_length=150)),
                ('fir_no', models.IntegerField()),
                ('password', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'main',
            },
        ),
        migrations.CreateModel(
            name='Suspect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_no', models.IntegerField()),
                ('other_info', models.TextField()),
            ],
            options={
                'db_table': 'suspect_info',
            },
        ),
    ]
