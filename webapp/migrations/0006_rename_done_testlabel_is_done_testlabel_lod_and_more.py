# Generated by Django 4.1.3 on 2023-01-01 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_testsample_control_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testlabel',
            old_name='done',
            new_name='is_done',
        ),
        migrations.AddField(
            model_name='testlabel',
            name='LOD',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='LOQ',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='labeling',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='margin',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='method_status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='regulation',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='sample_amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='specification',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlabel',
            name='test_result',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
