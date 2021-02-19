# Generated by Django 3.0.5 on 2021-02-12 14:23

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('piggy_bank_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('fromCif', models.TextField()),
                ('toCif', models.TextField()),
                ('amount', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('cif', models.TextField()),
                ('email_id', models.TextField()),
                ('name', djongo.models.fields.JSONField()),
                ('acc_type', models.TextField()),
                ('balance', models.BigIntegerField()),
                ('contact', models.TextField()),
                ('photo', models.BinaryField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]