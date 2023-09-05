from django.db.models.query import QuerySet

from .filters import BaseUserFilter
from .models import User

def user_get_login_data(*, user: User):
    return {
        "id": user.id,
        "email": user.email,
        "is_active": user.is_active,
        "is_staff": user.is_admin,
        "is_superuser": user.is_superuser,
    }


def user_list(*, filters=None) -> QuerySet[User]:
    filters = filters or {}

    qs = User.objects.all()

    return BaseUserFilter(filters, qs).qs
