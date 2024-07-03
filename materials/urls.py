from django.urls import path
from .views import RouterListCreateView, RouterDetailView, ONUListCreateView, ONUSerializerDetailView, DropCableListCreateView, DropCableDetailView, DropCableUsageRecordListCreateView, DropCableUsageRecordDetailView

urlpatterns = [
    path('routers/', RouterListCreateView.as_view(), name='router-list-create'),
    path('routers/<int:pk>/', RouterDetailView.as_view(), name='router-detail'),
    path('onus/', ONUListCreateView.as_view(), name='onu-list-create'),
    path('onus/<int:pk>/', ONUSerializerDetailView.as_view(), name='onu-detail'),
    path('drop-cables/', DropCableListCreateView.as_view(), name='drop-cable-list-create'),
    path('drop-cables/<int:pk>/', DropCableDetailView.as_view(), name='drop-cable-detail'),
    path('drop-cable-usage-records/', DropCableUsageRecordListCreateView.as_view(), name='drop-cable-usage-record-list-create'),
    path('drop-cable-usage-records/<int:pk>/', DropCableUsageRecordDetailView.as_view(), name='drop-cable-usage-record-detail'),
]
