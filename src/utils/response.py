from rest_framework.response import Response as DRFResponse
from rest_framework import status


class Response:
    
    @staticmethod
    def success(data=None, message="Success", status_code=status.HTTP_200_OK):
        return DRFResponse(
            {"success": True, "message": message, "data": data}, status=status_code
        )

    @staticmethod
    def error(message="Error", data=None, status_code=status.HTTP_400_BAD_REQUEST):
        return DRFResponse(
            {"success": False, "message": message, "data": data}, status=status_code
        )
