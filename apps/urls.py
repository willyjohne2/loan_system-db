from django.urls import path
from .views import (
    LoginView,
    UserListCreateView,
    LoanListCreateView,
    LoanProductListCreateView,
    RepaymentListCreateView,
    AuditLogListView,
    AdminListCreateView,
)

urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("admins/", AdminListCreateView.as_view(), name="admins"),
    path("users/", UserListCreateView.as_view(), name="users"),
    path("loans/", LoanListCreateView.as_view(), name="loans"),
    path("loan-products/", LoanProductListCreateView.as_view(), name="loan-products"),
    path("repayments/", RepaymentListCreateView.as_view(), name="repayments"),
    path("audit-logs/", AuditLogListView.as_view(), name="audit-logs"),
]
