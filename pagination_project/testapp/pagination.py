from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination,CursorPagination
class MyPagination(PageNumberPagination):
    page_size=5
    page_query_param='mypage' # default value is 'page'
    page_size_query_param='num'
    max_page_size=15
    last_page_strings=('endpage',) # default value is ('last')
    
class Mypagination2(LimitOffsetPagination):
    default_limit=15
    limit_query_param='mylimit'
    offset_query_param='myoffset'
    max_limit=20

class Mypagination3(CursorPagination):
    #pass # created is not available
    #ordering='-esal'
    ordering='esal'
    page_size=5