from rest_framework import serializers
from .models import (
    Admins,
    Users,
    Loans,
    LoanProducts,
    Repayments,
    Transactions,
    Notifications,
    AuditLogs,
    UserProfiles,
)


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "role",
            "is_verified",
            "is_blocked",
            "created_at",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class LoanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProducts
        fields = "__all__"


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"


class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayments
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLogs
        fields = "__all__"
