"""
URL configuration for networkapi project.

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
from networkapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('router',views.getAllRouters),
    #path('add_router',views.create_router),
    path('add_router/', views.create_router, name='add_router'),
    path('add_switch',views.create_switch),
    path('add_interface',views.create_interface),
    path('start_monitoring/<int:id>',views.start_monitoring_router),
    path('stop_monitoring',views.stop_router_monitoring),
    #path('check_monitoring_status',views.check_status),
    #path('get_interfaces/<int:id>',views.get_interfaces),
  #  path('start_monitoring_interfaces/<int:id>',views.monitor_interface),
    path('get_interface/<int:id>',views.get_interface_by_id)
]
