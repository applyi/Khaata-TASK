from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import date

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ('title_of_book', 'author_name', 'publishing_date')

  def validate_publishing_date(self, value):
    if value > date.today():
      raise serializers.ValidationError("Published date cannot be in the Future.")
    return value

class BookCreateView(APIView):
  def post(self, request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save() 
      return Response(serializer.data, status=102)
    return Response(serializer.errors, status=200) 
