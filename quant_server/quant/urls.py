from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    path('data_update', views.data_update, name='数据更新'),
    path('query_table', views.query_table, name='获取数据'),
    path('meta_tables', views.meta_tables),
    path('futu_info', views.futu_info),
    path('chart_data', views.chart_data),


]