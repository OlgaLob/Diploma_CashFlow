from django.urls import path
from django.conf.urls.static import static

from . import views
from .views import export_to_excel
from cashflowreport import settings

urlpatterns = [
    path("", views.Import_Excel_acc_pandas, name="Import_Excel_acc_pandas"),
    path('export/', export_to_excel, name='export_to_excel')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
