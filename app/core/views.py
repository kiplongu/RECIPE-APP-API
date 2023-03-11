"""
Core views for app.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def healt_check(request):
    """Returns successful request."""
    return Response({'healthy': True})
