# from .models import *
# from django.db.models import Count

from django.core.paginator import Paginator
from .models import Blog


def paginate_blogs(request, blogs, results):
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, results, allow_empty_first_page=True)

    blogs = paginator.get_page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1
    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, blogs
