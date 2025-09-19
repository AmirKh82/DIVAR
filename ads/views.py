from django.shortcuts import render
from .models import Category , City , ads
from django.http.response import JsonResponse , HttpResponse
from rest_framework.generics import ListAPIView,DestroyAPIView ,CreateAPIView,UpdateAPIView
from .serializers import Ads_Serializers
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
    
class All_ads_list(ListAPIView):
    queryset = ads.objects.all()
    serializer_class = Ads_Serializers

class Create_ads(CreateAPIView):
    queryset = ads.objects.all()
    serializer_class = Ads_Serializers

class Delete_ads(DestroyAPIView):
    queryset = ads.objects.all()
    serializer_class = Ads_Serializers

class Update_ads(UpdateAPIView):
    queryset = ads.objects.all()
    serializer_class = Ads_Serializers