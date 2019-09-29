# Generated by Django 2.2.5 on 2019-09-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('sn', models.AutoField(db_column='SN', primary_key=True, serialize=False)),
                ('date_field', models.TextField(blank=True, db_column='date\n', null=True)),
                ('channel_field', models.TextField(blank=True, db_column='channel\n', null=True)),
                ('country_field', models.TextField(blank=True, db_column='country\n', null=True)),
                ('os_field', models.TextField(blank=True, db_column='os\n', null=True)),
                ('impressions_field', models.TextField(blank=True, db_column='impressions\n', null=True)),
                ('clicks_field', models.TextField(blank=True, db_column='clicks\n', null=True)),
                ('installs_field', models.TextField(blank=True, db_column='installs\n', null=True)),
                ('spend_field', models.TextField(blank=True, db_column='spend\n', null=True)),
                ('revenue_field', models.TextField(blank=True, db_column='revenue\n', null=True)),
            ],
            options={
                'db_table': 'dataset',
                'managed': False,
            },
        ),
    ]