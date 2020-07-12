"""config URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from product.views import index, order_success_view
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('payments/complete/', order_success_view, name='order_check')
]

urlpatterns += static(
    # URL 앞부분이 /media/이면
    prefix=settings.MEDIA_URL,
    # document_root 위치에서 나머지 path에 해당하는 파일을 리턴
    document_root=settings.MEDIA_ROOT,
)