# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    username = models.CharField(unique=True, max_length=150)
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


class DevUserBsc(models.Model):
    mem_sno = models.DecimalField(db_column='MEM_SNO', primary_key=True, max_digits=20, decimal_places=0)  # Field name made lowercase.
    mem_curhold_sum = models.DecimalField(db_column='MEM_CURHOLD_SUM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mem_curchrg_sum = models.DecimalField(db_column='MEM_CURCHRG_SUM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mem_curaccum_sum = models.DecimalField(db_column='MEM_CURACCUM_SUM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mem_cursubs_sum = models.DecimalField(db_column='MEM_CURSUBS_SUM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mem_curgift_sum = models.DecimalField(db_column='MEM_CURGIFT_SUM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mem_curcashout_sum = models.DecimalField(db_column='MEM_CURCASHOUT_SUM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mem_curprch_sum = models.DecimalField(db_column='MEM_CURPRCH_SUM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mem_curpay_sum = models.DecimalField(db_column='MEM_CURPAY_SUM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mem_curgcard_sum = models.DecimalField(db_column='MEM_CURGCARD_SUM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sum_accu_startdttm = models.CharField(db_column='SUM_ACCU_STARTDTTM', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pay_pwd = models.CharField(db_column='PAY_PWD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    refund_bank_cd = models.CharField(db_column='REFUND_BANK_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refund_acc = models.CharField(db_column='REFUND_ACC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refund_acc_holder = models.CharField(db_column='REFUND_ACC_HOLDER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    svc_alarm_rcvyn = models.CharField(db_column='SVC_ALARM_RCVYN', max_length=1)  # Field name made lowercase.
    event_alarm_rcvyn = models.CharField(db_column='EVENT_ALARM_RCVYN', max_length=1)  # Field name made lowercase.
    mem_sece_dttm = models.CharField(db_column='MEM_SECE_DTTM', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mem_cert_nm = models.CharField(db_column='MEM_CERT_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mem_sex = models.CharField(db_column='MEM_SEX', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mem_nat = models.CharField(db_column='MEM_NAT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    self_cert_dt = models.CharField(db_column='SELF_CERT_DT', max_length=14, blank=True, null=True)  # Field name made lowercase.
    self_cert_ci = models.CharField(db_column='SELF_CERT_CI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    self_cert_di = models.CharField(db_column='SELF_CERT_DI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_dttm = models.CharField(db_column='REG_DTTM', max_length=14, blank=True, null=True)  # Field name made lowercase.
    reger = models.CharField(db_column='REGER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mod_dttm = models.CharField(db_column='MOD_DTTM', max_length=14, blank=True, null=True)  # Field name made lowercase.
    moder = models.CharField(db_column='MODER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1)  # Field name made lowercase.
    mem_dv_cd = models.CharField(db_column='MEM_DV_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dev_user_bsc'


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
