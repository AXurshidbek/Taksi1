from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drivers/', include("drivers.urls")),
    path('operators/', include("operators.urls")),
    path('users/', include("users.urls")),
    path('payments/', include("payments.urls")),
]

