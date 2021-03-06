"""IPFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
# from IPApp import views as user_view
# from django.contrib.auth import views as auth
# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls import patterns, include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('IPApp.urls')),
    path('accounts/', include('accounts.urls')),
    path('ipad/', include('ipad.urls')),
    # path('upload/', include('upload.urls')),
    # path('csvup/', include('csvup.urls'))


    # path('', include('IPApp.urls')),
    # path('login/', user_view.Login, name ='login'),
    # path('logout/', auth.LogoutView.as_view(template_name ='IPApp/index.html'), name ='logout'),
    # path('register/', user_view.register, name ='register'),
    # # path('signup/', signup_view, name='sign-up'),

]
# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = patterns('', (r'^', include('IPApp.urls')),) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
