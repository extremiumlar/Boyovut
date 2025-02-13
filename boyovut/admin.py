from django.contrib import admin
from .models import (
    Togarak_turlari,
    Togaraklar,
    Yangilik_va_tadbirlar,
    Numbers,
    Ustozlar,
    Iqtibostlar,
    Contact,
    RasmlarCategory,
    Rasmlar,
)
# Register your models here.

@admin.register(Togaraklar)
class TogaraklarAdmin(admin.ModelAdmin):
    list_display = ['nomi','turi','davomiyligi','boshlanish_sanasi','active']
    list_filter = ['turi','active','boshlanish_sanasi']
    #prepopulated_fields = {'slug': ('title',)}
    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'boshlanish_sanasi'
    search_fields = ['nomi']
    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active','boshlanish_sanasi']

@admin.register(Togarak_turlari)
class Togarak_turlariAdmin(admin.ModelAdmin):
    list_didplay = ['id','name']