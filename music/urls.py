from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home,name='home_url'),
    path('signup/', sign_up,name='signup_url'),
    path('login/', log_in,name='login_url'),
    path('logout/', log_out,name='logout_url'),
    path('about/', about,name='about_url')


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
