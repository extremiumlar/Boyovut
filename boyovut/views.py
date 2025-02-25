from django.shortcuts import render, redirect
from itertools import chain

from django.views.generic import TemplateView
from .models import (
    Iqtibostlar,
    Yangilik_va_tadbirlar,
    Togaraklar,
    Togarak_turlari,
    Numbers,
    Ustozlar,
    Contact,
    RasmlarCategory,
    Rasmlar,
)

# def home_view(request):
#
class HomePageView(TemplateView):
    template_name = 'home.html'

def HomeView(request):
    numbers = Numbers.objects.first()

    yangi = Togaraklar.objects.filter(status='New')[:6]
    davom_etayotgan = Togaraklar.objects.filter(status='Davom etayotgan')[:6]
    tugagan = Togaraklar.objects.filter(status='Yakunlangan')[:6]
    # print(yangi,"          ")
    # print(davom_etayotgan,"               ")
    # Ulanayotgan querysetlar sonini 6 taga yetkazish

    togaraklar = list(chain(yangi, davom_etayotgan, tugagan))[:6]
    # print(togaraklar)

    ustozlar = Ustozlar.objects.all().filter(active=True)[:4]
    iqtibostlar = Iqtibostlar.objects.all().filter(active=True)[:3]

    yangi = Yangilik_va_tadbirlar.objects.all().filter(active=True, status='New')[:6]
    tugagan = Yangilik_va_tadbirlar.objects.all().filter(active=True, status='Yakunlangan')[:6]

    yangiliklar = list(chain(yangi, tugagan))[:6]
    # print(numbers)

    context = {
        'numbers': numbers,
        'togaraklar': togaraklar,
        'ustozlar': ustozlar,
        'iqtibostlar': iqtibostlar,
        'yangiliklar': yangiliklar,

    }
    return render(request, 'home.html', context)

# to'garak va yangilik statuslarni avtomatik o'zgartirish uchun view ichiga kod
# iqtibostlar uchun alohida page qilish , hafta iqtibosti , oy iqtibosti , yil iqtibosti statuslarni modelga qo'shish
# rasmlarni yuklaganda kachestvani belgilab qo'yish yoki dastur davomida moslashtirish

# def togaraklarsingle_View(request, slug):
#     Togaraklar = Togaraklar.objects.all().filter(slug=slug)
#     return redirect('togaraklarsing', slug=slug)