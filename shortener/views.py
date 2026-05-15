from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from .models import Url
from .utils import generate_short_code
from urllib.parse import urlparse

@api_view(['POST'])
def shorten_url(request):
    long_url = request.data.get('longUrl')

    if not long_url:
        return Response(
            {'message' : 'longUrl is required'},
            status = status.HTTP_400_BAD_REQUEST
        )
    
    try:
        parsed = urlparse(long_url)
        if parsed.scheme not in ['http' , 'https']:
            return Response(
                {'message': 'URL must start with http:// or https://'},
                status = status.HTTP_400_BAD_REQUEST
            )
        if not parsed.netloc:
            return Response(
                {'message' : 'Please enter a valid URL'},
                status=status.HTTP_400_BAD_REQUEST
            )
    except Exception:
        return Response(
            {'message': 'Please enter a valid URL'},
            status=status.HTTP_400_BAD_REQUEST
        )
       
    existing_url = Url.objects.filter(long_url=long_url).first()
    if existing_url:
        return Response({
            'shortUrl': f'http://127.0.0.1:8000/api/v1/short-codes/{existing_url.short_code}',
            'longUrl':long_url,
            'createdAt':existing_url.created_at
        },status=status.HTTP_200_OK)
    
    short_code = generate_short_code()
    url = Url.objects.create(
        long_url = long_url,
        short_code = short_code
    )

    return Response({
        'shortUrl' : f'http://127.0.0.1:8000/api/v1/short-codes/{short_code}',
        'longUrl' : long_url,
        'createdAt' : url.created_at
    }, status = status.HTTP_201_CREATED)

@api_view(['GET'])
def redirect_url(request,short_code):
    try:
        url = Url.objects.get(short_code=short_code)
        return HttpResponsePermanentRedirect(url.long_url)
    except Url.DoesNotExist:
        return Response(
            {'message' : 'Short code not found'},
            status = status.HTTP_404_NOT_FOUND
        )
    
@api_view(['DELETE'])
def delete_url(request,short_code):
    try:
        url=Url.objects.get(short_code=short_code)
        url.delete()
        return Response(
            {'message':'URL deleted successfully'},
            status=status.HTTP_200_OK
        )
    except Url.DoesNotExist:
        return Response(
            {'message':'Short_code not found'},
            status=status.HTTP_404_NOT_FOUND
        )
