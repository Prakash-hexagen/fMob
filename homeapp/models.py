from django.db import models


class Contact(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    phone= models.IntegerField(max_length=10)
    subject= models.CharField(max_length=50)
    message= models.CharField(max_length=10000)
    date_time= models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact_us'