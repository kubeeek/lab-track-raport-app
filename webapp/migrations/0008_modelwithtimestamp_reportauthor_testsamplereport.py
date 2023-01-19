# Generated by Django 4.1.3 on 2023-01-15 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_testsample_options_testsample_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithTimestamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TestSampleReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=128)),
                ('supplier_address', models.CharField(max_length=128)),
                ('receiver_name', models.CharField(max_length=128)),
                ('receiver_address', models.CharField(max_length=128)),
                ('mechanism_name', models.CharField(max_length=128)),
                ('transport_method', models.CharField(choices=[('M1', 'Method 1'), ('M2', 'Method 2')], max_length=4)),
                ('author', models.ManyToManyField(to='webapp.reportauthor')),
                ('test_sample', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.testsample')),
            ],
        ),
    ]
