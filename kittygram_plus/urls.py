from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet

from rest_framework.authtoken import views


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
# router.register(r'mycats', LightCatViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]




'''
...
# При регистрации эндпоинтов с таким URL-префиксом
router.register(r'profile/(?P<username>[\w.@+-]+)/', AnyViewSet)
# ...вьюсет AnyViewSet будет получать на обработку все запросы с адресов
# /profile/toh@/
# /profile/nik.nik/
# /profile/leo/
# ...и подобных, ограниченных маской регулярного выражения.
'''
