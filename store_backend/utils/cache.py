from conf.settings import WORK_CACHE
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


def cache(time_cache):
    def cache_decorator(fun):
        work_cache = WORK_CACHE
        if work_cache:
            @method_decorator(cache_page(time_cache))
            def wrapper(request, *args, **kwargs):
                result = fun(request, *args, **kwargs)
                return result
        else:
            def wrapper(request, *args, **kwargs):
                result = fun(request, *args, **kwargs)
                return result

        return wrapper

    return cache_decorator
