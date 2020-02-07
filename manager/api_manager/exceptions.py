import json
import logging

from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status, exceptions
from rest_framework.exceptions import ValidationError
from rest_framework.utils import json
from rest_framework.views import exception_handler

from .error_codes_mapping import *


def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django Rest Framework that adds
    the `status_code` to the response and renames the `detail` key to `error`.
    """
    response = exception_handler(exc, context)
    data = dict()
    if response:
        data = json.loads(json.dumps(response.data))
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    code = code_status_mapping[status_code]["code"]
    title = code_status_mapping[status_code]["title"]

    if response is not None:
        status_code = response.status_code
        code = code_status_mapping[status_code]["code"]
        title = code_status_mapping[status_code]["title"]
        custom_errors = []
        for key, value in response.data.items():
            if isinstance(exc, Http404):
                error = {"field": key, "message": str(exc)}
                del data[key]
                custom_errors.append(error)
            else:
                error = {"field": key, "message": value}
                del data[key]
                custom_errors.append(error)
        data["errors"] = custom_errors
        if isinstance(exc, ValidationError):
            data["exception"] = "Validation Error"

    else:
        logging.error(exc, exc_info=True)
        error = {"field": "detail", "exception": str(exc)}
        data["errors"] = [error]
        data["exception"] = "Internal Server Error"
    data["code"] = code
    data["title"] = title

    return HttpResponse(
        json.dumps(data), content_type="application/json", status=status_code
    )


def resource_not_found_404(request):
    return JsonResponse(
        {"status_code": 404, "error": "The resource was not found"},
        status=status.HTTP_404_NOT_FOUND,
    )


def record_not_found_error(message):
    """
    :param message: the message to be printed
    """
    raise exceptions.NotFound(message)
