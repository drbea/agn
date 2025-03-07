
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("", include("home.urls")),
    path("products/", include("products.urls")),

    # path("shop/", include("shop.urls")),
    path("blog/", include("blog.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
