from django.contrib import admin
from .models import Togarak_turlari,Togaraklar
# Register your models here.

@admin.register(Togaraklar)
class TogaraklarAdmin(admin.ModelAdmin):
    list_display = ['nomi','turi','davomiyligi','publish_time','active']
    list_filter = ['turi','active','publish_time','boshlanish_sanasi']
    #prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'boshlanish_sanasi'
    search_fields = ['nomi']
    ordering = ['active','publish_time']
@admin.register(Togarak_turlari)
class Togarak_turlariAdmin(admin.ModelAdmin):
    list_didplay = ['id','name']