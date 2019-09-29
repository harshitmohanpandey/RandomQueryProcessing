# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dataset(models.Model):
    sn = models.AutoField(db_column='SN',primary_key=True)  # Field name made lowercase.
    date_field = models.TextField(db_column='date\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    channel_field = models.TextField(db_column='channel\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    country_field = models.TextField(db_column='country\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    os_field = models.TextField(db_column='os\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    impressions_field = models.TextField(db_column='impressions\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    clicks_field = models.TextField(db_column='clicks\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    installs_field = models.TextField(db_column='installs\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    spend_field = models.TextField(db_column='spend\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    revenue_field = models.TextField(db_column='revenue\n', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dataset'
