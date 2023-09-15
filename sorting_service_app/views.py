import importlib
import pkgutil
from inspect import getsource

import rest_framework.status as status
from django.http import HttpResponseServerError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import sorting_service_app.constants as sort_c

@api_view(['POST'])
def json_handler(request):
    json_data = request.data
    module_name = json_data['module']
    function_name = json_data['function']
    try:
        module = importlib.import_module(f"sorting_service_app.modules.{module_name}")
        function=getattr(module, function_name)
    except ImportError:
        return HttpResponseServerError("Unknown module NAME")
    except AttributeError:
        return HttpResponseServerError("Unknown function NAME")
    result = function(json_data)
    return Response(status=status.HTTP_200_OK, data=result)


def html_handler(request):
    function_list = []
    package_path = 'sorting_service_app.modules'
    package = importlib.import_module(package_path)
    for loader, module_name, is_pkg in pkgutil.walk_packages(package.__path__):
        if not is_pkg:
            module = importlib.import_module(f'{package_path}.{module_name}')
            for attr_name, attr in vars(module).items():
                if attr_name in sort_c.IGNORE_FUNCTIONS:
                    continue
                if callable(attr):
                    function_list.append({
                        'module_name': module_name,
                        'function_name': attr_name,
                        'description': attr.__doc__ or 'Нет описания',
                        'source_code': getsource(attr),
                    })

    context = {'function_list': function_list}
    return render(request, 'function_list.html', context)