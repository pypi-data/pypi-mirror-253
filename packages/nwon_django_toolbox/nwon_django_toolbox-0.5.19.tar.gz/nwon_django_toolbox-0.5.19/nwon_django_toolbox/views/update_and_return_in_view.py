from typing import Type

from django.db.models import Model, QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, Serializer

from nwon_django_toolbox.serializer.eager_loading_mixin import EagerLoadingMixin


def update_and_return_in_view(
    instance: Model,
    request: Request,
    update_serializer: Type[Serializer],
    return_serializer: Type[Serializer],
    partial: bool = False,
) -> Response:
    """
    A helper function that is supposed to be used in an update view.

    It takes an update_serializer that serializes the request.data
    and returns the updated model instance via the return_serializer.
    """

    serializer = update_serializer(
        data=request.data,
        instance=instance,
        partial=partial,
    )

    if serializer.is_valid():
        updated_instance = serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if issubclass(return_serializer, ModelSerializer) and issubclass(
        return_serializer, EagerLoadingMixin
    ):
        model: Type[Model] = return_serializer.Meta.model
        query_set: QuerySet = model.objects.filter(pk=updated_instance.pk)
        query_set = return_serializer.setup_eager_loading(query_set)

        data = return_serializer(query_set, many=True).data[0]
    else:
        data = return_serializer(instance=updated_instance).data

    return Response(
        data=data,
        status=status.HTTP_200_OK,
    )
