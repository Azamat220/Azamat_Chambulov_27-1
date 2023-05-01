"""
URL configuration for internet_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from internet_shop import settings
from products.views import (main_page_view, posts_view,
                            post_detial_view, post_create_view)
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('products/', posts_view),
    path('products/<int:id>/', post_detial_view),
    path('products/create/', post_create_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)