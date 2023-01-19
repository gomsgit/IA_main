from django.db import models


def upload_path(instance,filename):
    #print("inssss",instance)
    file_name = upload_category.objects.values("name","category")
    last_val = (list(file_name))[-1]

    print("lattt",last_val)

    final_path = last_val["name"]+"-"+last_val["category"]
    print("finallllllllllll",final_path)
    return '/'.join([final_path+"/"+filename])

class content_table(models.Model):
    bot_val=models.CharField(max_length=100)

class upload_image(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    images = models.ImageField(upload_to=upload_path,max_length=255,blank=True)
    upload_time = models.CharField(max_length=200)
    Analysis = models.CharField(max_length=100,default=True)

class upload_category(models.Model):
    name=models.CharField(max_length=100)
    category = models.CharField(max_length=100)