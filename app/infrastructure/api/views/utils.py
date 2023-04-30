from rest_framework.response import Response
from rest_framework import status
from app.error import Error


def body_validation_error_to_response(serializer) -> Response:
    return response(
        data=None,
        errors=[{"validation": serializer.errors}],
        status_code=status.HTTP_400_BAD_REQUEST,
    )


def result_error_to_response(error: Error) -> Response:
    return response(
        data=None,
        errors=[error.message],
        status_code=status.HTTP_400_BAD_REQUEST,
    )


def response(data={}, errors=[], status_code=status.HTTP_200_OK) -> Response:
    return Response(
        {
            "data": data,
            "errors": errors,
        },
        status=status_code,
    )
