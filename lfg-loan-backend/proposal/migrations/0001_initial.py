# Generated by Django 4.2.4 on 2023-08-29 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Automatically Approved', 'Automatically Approved'), ('Automatically Denied', 'Automatically Denied'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=30)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ProposalField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('field_type', models.CharField(choices=[('Text', 'Text'), ('Number', 'Number')], max_length=50)),
                ('required', models.BooleanField(default=True)),
            ],
        ),
    ]
