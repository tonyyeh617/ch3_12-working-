from django.db import models


class students(models.Model):
    cID = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=20, blank=False)
    cSex =  models.CharField(max_length=1, blank=False, default='F')
    # cBirthday = models.DateField(auto_now_add=True, null=False)
    #這個參數的預設值也為False，設定為True時，會在model物件第一次被建立時，
    #將欄位的值設定為建立時的時間，以後修改物件時，欄位的值不會再更新。
    #cBirthday = models.DateField(auto_now=True, null=False)
    #這個參數的預設值為false，當設定為true時，能夠在儲存該欄位時，
    #將其值設為目前時間，並且每次修改model，都會自動更新
    cBirthday = models.DateField(null=True, blank=True)
    cEmail = models.CharField(max_length=100, blank=False)
    cPhone = models.CharField(max_length=50, blank=False)
    cAddr = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"{self.name} ({self.id})"