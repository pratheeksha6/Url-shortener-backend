from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Url
from .utils import generate_short_code

@api_view(['POST'])
def shorten_url(request):
    long_url = request.data.get('longUrl')

    if not long_url:
        return Response(
            {'message' : 'longUrl is required'},
            status = status.HTTP_400_BAD_REQUEST
        )
    
    short_code = generate_short_code()
    url = Url.objects.create(
        long_url = long_url,
        short_code = short_code
    )

    return Response({
        'shortUrl' : f'http://localhost:8000/{short_code}',
        'longUrl' : long_url,
        'createdAt' : url.created_at
    }, status = status.HTTP_201_CREATED)
