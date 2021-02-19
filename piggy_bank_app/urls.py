from django.urls import path
from piggy_bank_app import views

urlpatterns = [
    path('viewCustomers', views.view_all_customers, name='View Customers'),
    path('', views.landing, name='Landing'),
    path('txHistory', views.txn_history, name='Transaction History'),
    path('transfer', views.money_trans, name='Funds Transfer'),
    path('customer_details', views.customer_details, name='Customer Details'),
    path(r'transaction_successful/', views.transaction_successful, name='Transaction Successful'),
    path('getTxns/<str:username>', views.getTxnData),
    path('submitTxn', views.submitTxn)
]