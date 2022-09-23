from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import ad.views
from HW_29 import settings
from user.views import LocationViewSet

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', ad.views.IndexView.as_view()),
	path('ad/', include('ad.urls')),
	path('cat/', include('category.urls')),
	path('user/', include('user.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = routers.SimpleRouter()
router.register('location', LocationViewSet)
urlpatterns += router.urls
