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


@admin.register(Togarak_turlari)
class Togarak_turlariAdmin(admin.ModelAdmin):
    list_didplay = ['id','name']
    search_fields = ['nomi']
    ordering = ['id']

@admin.register(Togaraklar)
class TogaraklarAdmin(admin.ModelAdmin):
    list_display = ['nomi','turi','davomiyligi','boshlanish_sanasi','active','status']
    list_filter = [
        'turi',
        'active',
        'davomiyligi',
        ('boshlanish_sanasi',admin.DateFieldListFilter),
    ]

    # slugni avtomatik to'ldirish keyinchalik

    prepopulated_fields = {'slug': ('nomi',)}

    # faqat o'qish uchun
    # readonly_fields = ['boshlanish_sanasi']

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'boshlanish_sanasi'
    search_fields = ['nomi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active','boshlanish_sanasi']


    # tahrirlash oynasni ochadi berilgan fieldlarni ustiga borganda
    list_display_links = ['nomi', 'turi']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active', 'davomiyligi']

    # nechta element ko'rsatishini belgilash
    # list_per_page = 20



    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('nomi', 'turi', 'davomiyligi', 'manzil', 'boshlanish_sanasi', 'active','status')
        }),
        ('Qo\'shimcha ma\'lumotlar', {
            'classes': ('collapse',),  # Qisqartirilgan (collapse) holda ko'rsatish
            'fields': ('body', 'body_small', 'image')
        }),
    )
    # avtomatik to'ldirish faqat fk bilan bo'glanganlar uchun
    # searchfieldni qo'shib qo'yish kerak bog'langan modelga
    autocomplete_fields = ['turi']



@admin.register(RasmlarCategory)
class RasmlarCategoryAdmin(admin.ModelAdmin):
    list_didplay = ['id','name']
    search_fields = ['name']

@admin.register(Rasmlar)
class RasmlarAdmin(admin.ModelAdmin):

    list_display = ['name','tarif','turi','publish_time','active']
    list_filter = [
        'turi',
        'active',
        ('publish_time',admin.DateFieldListFilter),
    ]

    #slugni avtomatik to'ldirish keyinchalik
    #prepopulated_fields = {'slug': ('title',)}

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['name']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active','publish_time']


    # tahrirlash oynasni ochadi berilgan fieldlarni ustiga borganda
    list_display_links = ['name', 'turi','tarif']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']

    # nechta element ko'rsatishini belgilash
    # list_per_page = 20



    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name', 'tarif', 'turi', 'active')
        }),
        ('Qo\'shimcha ma\'lumotlar', {
            'classes': ('collapse',),  # Qisqartirilgan (collapse) holda ko'rsatish
            'fields': ('image', 'image_small')
        }),
    )
    # avtomatik to'ldirish faqat fk bilan bo'glanganlar uchun
    # searchfieldni qo'shib qo'yish kerak bog'langan modelga
    autocomplete_fields = ['turi']


@admin.register(Yangilik_va_tadbirlar)
class Yangilik_va_tadbirlarAdmin(admin.ModelAdmin):
    list_display = ['nomi','manzil','boshlanish_sanasi','active','status']
    list_filter = [
        'active',
        ('boshlanish_sanasi',admin.DateFieldListFilter),
    ]

    #slugni avtomatik to'ldirish keyinchalik
    prepopulated_fields = {'slug': ('nomi',)}

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'boshlanish_sanasi'
    search_fields = ['nomi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active','boshlanish_sanasi']


    # tahrirlash oynasni ochadi berilgan fieldlarni ustiga borganda
    list_display_links = ['nomi', 'manzil']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']

    # nechta element ko'rsatishini belgilash
    # list_per_page = 20



    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('nomi', 'slug', 'manzil', 'boshlanish_sanasi', 'active', 'status')
        }),
        ('Qo\'shimcha ma\'lumotlar', {
            'classes': ('collapse',),  # Qisqartirilgan (collapse) holda ko'rsatish
            'fields': ('body', 'body_small', 'image')
        }),
    )

@admin.register(Ustozlar)
class UstozlarAdmin(admin.ModelAdmin):
    list_display = ['name','last_name','father_name','publish_time','active']
    list_filter = [
        'active',
        ('publish_time',admin.DateFieldListFilter),
    ]

    #slugni avtomatik to'ldirish keyinchalik
    #prepopulated_fields = {'slug': ('title',)}

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['name','last_name','father_name']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active','publish_time']


    # tahrirlash oynasni ochadi berilgan fieldlarni ustiga borganda
    list_display_links = ['name', 'last_name','father_name']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']

    # nechta element ko'rsatishini belgilash
    # list_per_page = 20



    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name', 'last_name', 'father_name', 'active')
        }),
        ('Qo\'shimcha ma\'lumotlar', {
            'classes': ('collapse',),  # Qisqartirilgan (collapse) holda ko'rsatish
            'fields': ('body', 'facebook', 'telegram', 'twitter','google', 'image')
        }),
    )

@admin.register(Iqtibostlar)
class IqtibostlarAdmin(admin.ModelAdmin):
    list_display = ['ism','familiya','iqtibost_egasining_ismi','iqtibost_egasining_familiyasi','publish_time', 'active']
    list_filter = [
        'active',
        ('publish_time',admin.DateFieldListFilter),
    ]

    #slugni avtomatik to'ldirish keyinchalik
    #prepopulated_fields = {'slug': ('title',)}

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['ism','iqtibost_egasining_ismi']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['active','publish_time']


    # tahrirlash oynasni ochadi berilgan fieldlarni ustiga borganda
    list_display_links = ['ism','familiya','iqtibost_egasining_ismi','iqtibost_egasining_familiyasi']

    # quyidagi fieldlarni jadvalni o'zida to'g'irlash imkonini beradi editpagega kirmasdan
    list_editable = ['active']

    # nechta element ko'rsatishini belgilash
    # list_per_page = 20



    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('ism','familiya','iqtibost_egasining_ismi','iqtibost_egasining_familiyasi', 'active')
        }),
        ('Qo\'shimcha ma\'lumotlar', {
            'classes': ('collapse',),  # Qisqartirilgan (collapse) holda ko'rsatish
            'fields': ('body', 'email', 'image')
        }),
    )




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ['name','email','message','publish_time']
    list_filter = [
        'name',
        ('publish_time',admin.DateFieldListFilter),
    ]

    #slugni avtomatik to'ldirish keyinchalik
    #prepopulated_fields = {'slug': ('title',)}

    # faqat o'qish uchun
    # readonly_fields = ['boshlanish_sanasi']

    # data_hierarchy yil oy kun bo'yicha ajratish uchun ishlatiladi
    date_hierarchy = 'publish_time'
    search_fields = ['name']

    # ordering tartiblash uchun ishlatiladi birinchi active bo'yicha keyin boshlanish_sanasi
    ordering = ['publish_time']


    # tahrirlash oynasni ochadi berilgan fieldlarni ustiga borganda
    list_display_links = ['name', 'email']

    # nechta element ko'rsatishini belgilash
    # list_per_page = 20


admin.site.register(Numbers)








