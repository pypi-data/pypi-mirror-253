from graphene_django import DjangoObjectType
from graphene_django_cud.mutations import (
    DjangoBatchCreateMutation,
    DjangoBatchDeleteMutation,
    DjangoBatchPatchMutation,
)

from ..models import Room
from .base import (
    DjangoFilterMixin,
    PermissionBatchDeleteMixin,
    PermissionBatchPatchMixin,
    PermissionsTypeMixin,
)


class RoomType(PermissionsTypeMixin, DjangoFilterMixin, DjangoObjectType):
    class Meta:
        model = Room
        fields = ("id", "name", "short_name")
        filter_fields = {
            "id": ["exact", "lte", "gte"],
            "name": ["icontains"],
            "short_name": ["icontains"],
        }

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset  # FIXME filter this queryset based on permissions


class RoomBatchCreateMutation(PermissionBatchPatchMixin, DjangoBatchCreateMutation):
    class Meta:
        model = Room
        permissions = ("core.create_room",)
        only_fields = ("id", "name", "short_name")


class RoomBatchDeleteMutation(PermissionBatchDeleteMixin, DjangoBatchDeleteMutation):
    class Meta:
        model = Room
        permissions = ("core.delete_room",)


class RoomBatchPatchMutation(PermissionBatchPatchMixin, DjangoBatchPatchMutation):
    class Meta:
        model = Room
        permissions = ("core.change_room",)
        only_fields = ("id", "name", "short_name")
