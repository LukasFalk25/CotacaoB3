from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/ativos/')),
    path('admin/', admin.site.urls),
    path('ativos/', include('ativos.urls')),
]
