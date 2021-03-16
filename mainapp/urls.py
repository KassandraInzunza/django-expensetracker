from django.urls import path
from . import views

urlpatterns=[
    path(r'/',views.index, name='main-index'),
    path(r'summary/', views.SummaryListView.as_view(), name='main-summary'),
    path(r'expense/', views.ExpenseCreate.as_view(), name='main-expense-create'),
]