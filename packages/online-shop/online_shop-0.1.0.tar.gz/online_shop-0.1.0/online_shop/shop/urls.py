from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from online_shop.users.views import admin_logout_view

urlpatterns = [
    path("admin/logout/", admin_logout_view),
    path("admin/", admin.site.urls),
    path("categories/", include("online_shop.categories.urls")),
    path("orders/", include("online_shop.orders.urls")),
    path("products/", include("online_shop.products.urls")),
    path("users/", include("online_shop.users.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
