from rest_framework.pagination import PageNumberPagination


class PageLimitPagination(PageNumberPagination):
    # PAGE_SIZE = 6 указан в settings.py
    page_size_query_param = 'limit'
