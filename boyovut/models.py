from django.utils import timezone

from django.db import models
from django.urls import reverse
# Create your models here.

class Togarak_turlari(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Yonalish turlari'
        verbose_name = 'Yonalish turi'

class Togaraklar(models.Model):
    nomi = models.CharField(max_length=100)
    image = models.ImageField(upload_to='togarak_images')
    turi = models.ForeignKey(Togarak_turlari, on_delete=models.PROTECT, null=True,blank=True)
    manzil = models.CharField(max_length=150)
    oquvchilar_soni = models.PositiveIntegerField(blank=True,null=True)
    davomiyligi = models.CharField(max_length=150,blank=True,null=True)
    slug = models.SlugField(max_length=150,unique=True)
    boshlanish_sanasi = models.DateField(default=timezone.now)
    body = models.TextField()
    body_small = models.TextField(max_length=250)
    active = models.BooleanField(default=True)
    # publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi
    def get_absolute_url(self):
        pass
        # return reverse("yonalish_detail", kwargs={"slug": self.slug})
    class Meta:
        ordering = ['-boshlanish_sanasi']
        verbose_name_plural = "To'garaklar"
        verbose_name = "To'garak"

class Yangilik_va_tadbirlar(models.Model):
    # class Status(models.TextChoices):
    #     Draft = 'DF', 'Draft'
    #     Published = 'PB', 'Published'
    # status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)
    nomi = models.CharField(max_length=100)
    image = models.ImageField(upload_to='yangilik_images')
    manzil = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,unique=True)
    boshlanish_sanasi = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    body_small = models.TextField(max_length=250)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.nomi
    def get_absolute_url(self):
        pass
        # return reverse("yonalish_detail", kwargs={"slug": self.slug})
    class Meta:
        ordering = ['-boshlanish_sanasi']
        # ordering = ['publish_time'] # birinchi yozilgna birinchi chiqadi
        verbose_name_plural = "Yangiliklar va tadbirlar"
        verbose_name = "Yangilik va tadbir"

class Numbers(models.Model):
    fanlar = models.PositiveIntegerField(default=0)
    oquvchilar = models.PositiveIntegerField(default=0)
    labaratoriyalar = models.PositiveIntegerField(default=0)
    oqituvchilar = models.PositiveIntegerField(default=0)


class Ustozlar(models.Model):
    # class Status(models.TextChoices):
    #     Draft = 'DF', 'Draft'
    #     Published = 'PB', 'Published'
    # status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='ustozlar_images')
    active = models.BooleanField(default=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    facebook = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    telegram = models.URLField(blank=True,null=True)
    google = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        pass
        # return reverse("yonalish_detail", kwargs={"slug": self.slug})
    class Meta:
        ordering = ['-publish_time']
        # ordering = ['publish_time'] # birinchi yozilgna birinchi chiqadi
        verbose_name_plural = "O'qituvchilar"
        verbose_name = "O'qituvchi"

class Iqtibostlar(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    iqtibost_egasining_ismi = models.CharField(max_length=100)
    iqtibost_egasining_familiyasi = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='iqtibost_images')
    active = models.BooleanField(default=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.ism} {self.iqtibost_egasining_ismi} {self.iqtibost_egasining_familiyasi}"

    class Meta:
        ordering = ['-publish_time']
        verbose_name_plural = "Iqtiboslar"
        verbose_name = "Iqtibos"

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Bog'lanish"
        verbose_name_plural = "Bog'lanish"

class RasmlarCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Rasm turlari"
        verbose_name_plural = "Rasm turlari"

class Rasmlar(models.Model):
    name = models.CharField(max_length=100)
    tarif = models.CharField(max_length=100)
    image_small = models.ImageField(upload_to='rasmlar_small')
    image = models.ImageField(upload_to='rasmlar_big')
    turi = models.ForeignKey(RasmlarCategory,on_delete=models.PROTECT, null=True,blank=True)
    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"










































