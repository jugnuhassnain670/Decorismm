
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Decorism Admin"
admin.site.site_title = "Decorism Admin Portal"
admin.site.index_title = "Welcome to Decorism Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendors/', include('vendor.urls')),
    path('cart/', include('cart.urls')),
    path('product/', include('product.urls')),
    path('blog/', include('blog.urls')),
    path('', include('core.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
