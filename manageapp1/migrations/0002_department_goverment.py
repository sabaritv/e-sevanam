# Generated by Django 4.0 on 2022-01-31 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manageapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Goverment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manageapp1.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='govt', to='manageapp1.login')),
            ],
        ),
    ]