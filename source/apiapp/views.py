import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


def is_number(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def calculator(request, operation):
    if request.method == 'POST':
        if request.body:
            try:
                answer = json.loads(request.body)
                if is_number(answer['A']) and is_number(answer['B']):
                    if operation == 'add':
                        answer = float(answer['A']) + float(answer['B'])
                    elif operation == 'subtract':
                        answer = float(answer['A']) - float(answer['B'])
                    elif operation == 'multiply':
                        answer = float(answer['A']) * float(answer['B'])
                    elif operation == 'divide' and answer['B'] != 0:
                        answer = float(answer['A']) / float(answer['B'])
                    return JsonResponse({'answer': float(answer)}, safe=False)
                response = JsonResponse({'error': 'Value error!'})
                response.status_code = 400
                return response
            except:
                response = JsonResponse({'error': 'Value error!'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response


@csrf_exempt
def add_view(request, *args, **kwargs):
    return calculator(request, 'add')


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    return calculator(request, 'subtract')


@csrf_exempt
def multiply_view(request, *args, **kwargs):
    return calculator(request, 'multiply')


@csrf_exempt
def divide_view(request, *args, **kwargs):
    return calculator(request, 'divide')


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')
