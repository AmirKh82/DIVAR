from django.urls import path , include
from .views import show_all_ads ,show_city_ads , show_category_ads ,delete_ads_by_id

urlpatterns = [
    path('ads-list', show_all_ads),
    path('city/<str:city>', show_city_ads),
    path('category/<str:category>', show_category_ads),
    path('delete/<str:id>', delete_ads_by_id),
]