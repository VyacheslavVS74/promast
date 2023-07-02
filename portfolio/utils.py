from .models import Works
from django.db.models import Q
from django.core.paginator import Paginator


def search_works(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    works = Works.objects.distinct().filter(Q(title__iregex=search_query) |
                                            Q(material__iregex=search_query))

    return works, search_query


def paginate_works(request, works, results):
    page = request.GET.get('page', 1)
    paginator = Paginator(works, results, allow_empty_first_page=True)

    works = paginator.get_page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1
    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, works
