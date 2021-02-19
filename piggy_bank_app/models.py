from djongo import models
from django import forms

class UserData(models.Model):
    _id = models.ObjectIdField()
    cif = models.TextField()
    email_id = models.TextField()
    name = models.JSONField()
    acc_type = models.TextField()
    balance = models.BigIntegerField()
    contact = models.TextField()
    # accounts = models.ArrayField(
    #     model_container=Account,
    #     model_form_class=AccountForm
    # )
    # contact = models.ArrayField(
    #     model_container=Contact,
    #     model_form_class=ContactForm
    # )
    photo = models.BinaryField()
    #transactions = models.JSONField()
    objects = models.DjongoManager()

class Transactions(models.Model):
    _id = models.ObjectIdField()
    fromCif = models.TextField()
    toCif = models.TextField()
    amount = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    objects = models.DjongoManager()