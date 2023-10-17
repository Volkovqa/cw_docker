from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_params = 'page_size'
    max_page_size = 20