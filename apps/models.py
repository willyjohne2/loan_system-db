# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admins(models.Model):
    id = models.UUIDField(primary_key=True)
    full_name = models.TextField()
    email = models.TextField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.TextField()
    password_hash = models.TextField()
    is_verified = models.BooleanField(blank=True, null=True)
    is_blocked = models.BooleanField(blank=True, null=True)
    failed_login_attempts = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'admins'


class AuditLogs(models.Model):
    id = models.UUIDField(primary_key=True)
    admin = models.ForeignKey(Admins, models.DO_NOTHING, blank=True, null=True)
    action = models.TextField()
    table_name = models.TextField()
    record_id = models.UUIDField(blank=True, null=True)
    old_data = models.JSONField(blank=True, null=True)
    new_data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'audit_logs'


class LoanProducts(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    min_amount = models.DecimalField(max_digits=12, decimal_places=2)
    max_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration_months = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'loan_products'


class Loans(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    loan_product = models.ForeignKey(LoanProducts, models.DO_NOTHING)
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration_months = models.IntegerField()
    status = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'loans'


class Notifications(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    message = models.TextField()
    is_read = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notifications'


class RepaymentSchedule(models.Model):
    id = models.UUIDField(primary_key=True)
    loan = models.ForeignKey(Loans, models.DO_NOTHING)
    installment_number = models.IntegerField()
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'repayment_schedule'


class Repayments(models.Model):
    id = models.UUIDField(primary_key=True)
    loan = models.ForeignKey(Loans, models.DO_NOTHING)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.TextField(blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    reference_code = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'repayments'


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    type = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'transactions'


class UserProfiles(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    national_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    employment_status = models.TextField(blank=True, null=True)
    monthly_income = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_profiles'


class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    full_name = models.TextField()
    phone = models.CharField(unique=True, max_length=20)
    email = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'
