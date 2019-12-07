from django.db import models
from ecount.utils import uuid_upload_to
from django.urls import reverse

class Shop(models.Model):
    거래처코드 = models.CharField(max_length=10, primary_key=True)
    거래처명 = models.CharField(max_length=20)
    내용 = models.TextField()
    생성시간 = models.DateTimeField(auto_now_add=True)
    수정시간 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.거래처코드

    def get_absolute_url(self):
        return reverse('myapp:shop_list')

class Product(models.Model):
    품목코드= models.CharField(max_length=20)
    품목명= models.CharField(max_length=20)
    품목구분= models.CharField(max_length=20)
    거래처코드 = models.ForeignKey(Shop, on_delete=models.CASCADE)
    색상= models.CharField(max_length=20, blank=True)
    단위= models.CharField(max_length=20, blank=True)
    개수 = models.IntegerField()
    입고단가 = models.IntegerField()
    이미지 = models.ImageField( blank=True, upload_to=uuid_upload_to)
    내용 = models.TextField(blank=True)
    생성시간 = models.DateTimeField(auto_now_add=True)
    수정시간 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.품목코드