from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import FeedbackSerializer, FeedbackTypeSerializer
from .models import FeedbackType


class FeedbackView(APIView):
    """View для обработки данных с формы обратной связи."""

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class FeedbackTypeView(APIView):
    """View для получения типов обратной связи."""

    def get(self, request, *args, **kwargs):
        types = FeedbackType.objects.all()
        serializer = FeedbackTypeSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
