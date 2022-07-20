# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256)
    completed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_task'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    userid = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EvspBoard(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    register_dttm = models.DateTimeField()
    user = models.ForeignKey('EvspEvuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'evsp_board'


class EvspCardinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cardname = models.CharField(max_length=64)
    cardtag = models.CharField(max_length=64)
    cardstatus = models.CharField(max_length=64)
    register_dttm = models.DateTimeField()
    userid = models.ForeignKey('EvspEvuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'evsp_cardinfo'


class EvspCharginginfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    energy = models.IntegerField()
    amount = models.IntegerField()
    start_dttm = models.DateTimeField()
    end_dttm = models.DateTimeField()
    cpname = models.ForeignKey('EvspEvcharger', models.DO_NOTHING)
    userid = models.ForeignKey('EvspEvuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'evsp_charginginfo'


class EvspEvcharger(models.Model):
    id = models.BigAutoField(primary_key=True)
    cpname = models.CharField(max_length=64)
    cpnumber = models.CharField(max_length=64)
    partner_id = models.CharField(max_length=128)
    public_use = models.IntegerField()
    cpstatus = models.CharField(max_length=64)
    connector_id_1 = models.CharField(max_length=64)
    connector_id_1_status = models.CharField(max_length=64)
    connector_id_2 = models.CharField(max_length=64)
    connector_id_2_status = models.CharField(max_length=64)
    address = models.TextField()
    manager_id = models.CharField(max_length=128)
    cpversion = models.CharField(max_length=64)
    register_dttm = models.DateTimeField()
    last_modified_dttm = models.DateTimeField()
    fw_version = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'evsp_evcharger'


class EvspEvuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    usernumber = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    address = models.TextField()
    level = models.CharField(max_length=8)
    last_use_dttm = models.DateTimeField()
    register_dttm = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'evsp_evuser'


class EvspMsglog(models.Model):
    id = models.BigAutoField(primary_key=True)
    msg_direction = models.IntegerField()
    msg_name = models.CharField(max_length=128)
    msg_content = models.TextField()
    connection_id = models.CharField(max_length=128)
    register_dttm = models.DateTimeField()
    cpname = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'evsp_msglog'


class EvspTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    register_dttm = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'evsp_tag'