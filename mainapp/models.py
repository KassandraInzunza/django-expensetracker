from django.db import models

# Create your models here.

class TransactionModel(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    amount = models.IntegerField()

    class Meta:
        db_table = "transactions"
        managed = True

class MembersModel(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=25)
    group = models.CharField(max_length=25)

    class Meta:
        db_table = "members"
        managed = True