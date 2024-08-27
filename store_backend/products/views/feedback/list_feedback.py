from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from products.serializers.feedback import ListFeedbackSerializers
from products.services.feedback import FeedbackListService


class ListFeedbackView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        page_size = request.query_params.get('page_size')
        pagination = PageNumberPagination()
        feedback_queryset = FeedbackListService.execute({})

        if page_size and int(page_size) > 0:
            pagination.page_size = page_size
        paginate_queryset = pagination.paginate_queryset(feedback_queryset, request)
        serializers = ListFeedbackSerializers(paginate_queryset, many=True).data
        return pagination.get_paginated_response(serializers)
