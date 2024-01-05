from django.urls import path
from .views import index, page1, top_sellers, advertisement_post, advertisement_detail


urlpatterns = [
    path('', index, name='main-page'),
    path('page1/', page1),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='adv-post'),
    path('advertisement/<int:pk>', advertisement_detail, name='adv-detail'),
]
