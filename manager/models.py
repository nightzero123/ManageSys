from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=32)
    user_role_id = models.IntegerField()
    user_password = models.CharField(max_length=32)

class ContractAppendix(models.Model):
    file_id=models.IntegerField(primary_key=True)
    file_url=models.CharField(max_length=128)

class Customer(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=32)
    customer_addr=models.CharField(max_length=128)
    customer_tel=models.CharField(max_length=32)
    customer_fax=models.CharField(max_length=32)
    customer_post=models.CharField(max_length=32)
    customer_bank=models.CharField(max_length=32)
    customer_account=models.CharField(max_length=32)

class Contract(models.Model):
    contract_name = models.CharField(max_length=32)
    contract_id = models.IntegerField(primary_key=True)
    contract_description = models.CharField(max_length=128)
    contract_user_id=models.ForeignKey(User, to_field="user_id",on_delete=models.CASCADE, related_name='contract_related_user')
    contract_create_time=models.DateTimeField()
    contract_status=models.IntegerField()
    contract_begin_time=models.DateTimeField()
    contract_end_time=models.DateTimeField()
    file_id=models.ForeignKey(ContractAppendix, to_field="file_id", on_delete=models.CASCADE, related_name='contract_related_file')
    contract_consumer_id=models.ForeignKey(Customer, to_field="customer_id",on_delete=models.CASCADE, related_name='contract_related_customer')

class RoleP(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_permission = models.IntegerField()


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=32)
    role_describe=models.CharField(max_length=128)

class OperationHistroy(models.Model):
    contract_id=models.ForeignKey(Contract,to_field="contract_id",on_delete=models.CASCADE, related_name='contract_related_operation')
    user_id=models.ForeignKey(User,to_field="user_id", on_delete=models.CASCADE, related_name='user_related_operation')
    op_type=models.IntegerField()
    context=models.CharField(max_length=128)
    op_time=models.DateTimeField()





