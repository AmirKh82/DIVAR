from django.urls import path , include
from .views import show_all_ads,show_city_ads,show_category_ads,delete_ads_by_id,All_ads_list,Create_ads,Delete_ads,Update_ads

urlpatterns = [
    path('ads-list', show_all_ads),
    path('city/<str:city>', show_city_ads),
    path('category/<str:category>', show_category_ads),
    path('delete/<str:id>', delete_ads_by_id),
    path('delete/<str:id>', delete_ads_by_id),
    path('ads-list-rest', All_ads_list.as_view()),
    path('create-ads-rest', Create_ads.as_view()),
    path('delete-ads-rest/<str:pk>', Delete_ads.as_view()),
    path('update-ads-rest/<str:pk>', Update_ads.as_view()),
]