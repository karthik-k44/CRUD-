"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from crud.views import Mobilesview,Mobilelist,Mobiledelete,Mobiledetails,Mobileupdate,Signup,Login,Logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mobiles/', Mobilesview.as_view(), name='mobile-add'),
    path('mobile/list/',Mobilelist.as_view(),name='mobile-al'),
    path('mobile/<int:id>',Mobiledelete.as_view(),name='mobile-del'),
    path('mobiledeta/<int:id>',Mobiledetails.as_view(),name='mobile-deta'),
    path('mobileadd/<int:id>',Mobileupdate.as_view(),name='mobile-update'),
    path('reg/',Signup.as_view()),
    path('',Login.as_view(),name="login"),
    path('logout/',Logout.as_view(),name="logout")
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
