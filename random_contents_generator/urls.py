from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Random Contents Generator Admin'
admin.site.index_title = 'Random Contents Generator Manager'


urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
