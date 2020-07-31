from rest_framework.pagination import LimitOffsetPagination


class GetChartTwoSetPagination(LimitOffsetPagination):
    '''default_limit:默认返回条数'''
    default_limit = 100
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 1000