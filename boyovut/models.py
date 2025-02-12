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

class Togaraklar(models.Model):
    nomi = models.CharField(max_length=100)
    image = models.ImageField(upload_to='togarak_images')
    turi = models.ForeignKey(Togarak_turlari, on_delete=models.CASCADE)
    manzil = models.CharField(max_length=150)
    oquvchilar_soni = models.IntegerField(blank=True,null=True)
    davomiyligi = models.CharField(max_length=150,blank=True,null=True)
    boshlanish_sanasi = models.DateField(default=timezone.now)
    body = models.TextField()
    body_small = models.TextField(max_length=250)
    active = models.BooleanField(default=True)
    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi
    def get_absolute_url(self):
        pass
        # return reverse("yonalish_detail", kwargs={"slug": self.slug})
    class Meta:
        ordering = ['-publish_time']
        verbose_name_plural = "Tog'araklar"

class Yangilik_va_tadbirlar(models.Model):
    nomi = models.CharField(max_length=100)
    image = models.ImageField(upload_to='togarak_images')
    manzil = models.CharField(max_length=150)
    boshlanish_sanasi = models.DateField(default=timezone.now)
    body = models.TextField()
    body_small = models.TextField(max_length=250)
    active = models.BooleanField(default=True)
    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi
    def get_absolute_url(self):
        pass
        # return reverse("yonalish_detail", kwargs={"slug": self.slug})
    class Meta:
        ordering = ['-publish_time']
        verbose_name_plural = "Tog'araklar"









































