# Generated by Django 4.0.3 on 2022-04-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIR', '0013_alter_attachmentmodel_id_alter_complainant_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complainant',
            name='addhar_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='complainant',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='complainant',
            name='district',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='complainant',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='complainant',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='complainant',
            name='pincode',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='complainant',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
