from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import serializers
from app.infrastructure.api.serializers import ItemSerializer
from app.application import List as ListApplication
from .utils import response, body_validation_error_to_response, result_error_to_response


class CreateBodySerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
    list_id = serializers.CharField(max_length=100)


class ItemList(generics.GenericAPIView):
    def post(self, request) -> Response:
        serializer = CreateBodySerializer(data=request.data)

        if serializer.is_valid() == False:
            return body_validation_error_to_response(serializer)

        save_result = ListApplication().create_item(
            serializer.validated_data["text"],
            serializer.validated_data["list_id"],
        )

        if save_result.is_err():
            return result_error_to_response(save_result.err())

        return response(
            data=ItemSerializer(save_result.ok()).data,
            errors=[],
            status_code=status.HTTP_201_CREATED,
        )
