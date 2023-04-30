from rest_framework import status, generics
from rest_framework.response import Response
from app.infrastructure.api.serializers import ListSerializer
from app.application import List as ListApplication
from .utils import response, body_validation_error_to_response, result_error_to_response


class ListDetails(generics.GenericAPIView):
    def get(self, request, id) -> Response:
        list_result = ListApplication().find(id)

        if list_result.is_err():
            return result_error_to_response(list_result.err())

        return response(
            data=ListSerializer(list_result.ok()).data,
            errors=[],
            status_code=status.HTTP_201_CREATED,
        )
