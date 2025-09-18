from django.shortcuts import render
from .models import Category , City , ads
from django.http.response import JsonResponse , HttpResponse
# Create your views here.

def show_all_ads(request):
    adv = ads.objects.all().values()
    Ads = list(adv)
    return JsonResponse(Ads,safe=False)

def show_city_ads(request,city):
    adv_city = ads.objects.filter(city__name__iexact=city).values()
    adv = list(adv_city)
    return JsonResponse(adv,safe=False)

def show_category_ads(request,category):
    adv_category = ads.objects.filter(category__title__iexact=category).values()
    adv = list(adv_category)
    return JsonResponse(adv,safe=False)

def delete_ads_by_id(request,id):
    try:
        ads.objects.get(id=id).delete()
        return HttpResponse('the ads deleted')
    except ads.DoesNotExist:
        return HttpResponse('the ads not exists')