import random
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


def process_response_for_get_based_on_serialized_data(data_objects, model_serializer):
    serializer = model_serializer(data_objects, many=True)

    return Response(serializer.data)


def process_response_for_post_based_on_serialized_data(request, model_serializer):
    serializer = model_serializer(data=request.data, many=True)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def process_response_for_get_item_based_on_serialized_data(model, pk, model_serializer):
    post = get_object_or_404(model, pk=pk)
    serializer = model_serializer(post)

    return Response(serializer.data)


def process_response_for_put_based_on_serialized_data(model, pk, model_serializer):
    post = get_object_or_404(model, pk=pk)
    serializer = model_serializer(data=post, many=True)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def process_delete_item_based_on_pk(post):
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
