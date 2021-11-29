#from django.forms.widgets import NullBooleanSelect
#from .view import *
from django.http import HttpResponse, Http404


def managerdecorator(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            groups = None
            check = False

            if request.user.groups.exists:
                groups = request.user.groups.all()
                for group in groups:
                    if group.name in allowed_roles:
                        check = True

                        break
            if check:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You do not have permission to view this page")

        return wrapper_func

    return decorator
