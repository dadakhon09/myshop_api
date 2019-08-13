from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
)

class UserPageNumberPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 10

