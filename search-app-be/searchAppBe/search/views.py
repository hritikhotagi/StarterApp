from django.shortcuts import render
from django.http import JsonResponse

def search(request):
    try:
        data = request.POST
        search_term = data.get('searchTerm', '')

        # Implement your search logic here
        # You can perform database queries or other search-related operations

        # For simplicity, just returning the search term in this example
        response = {'result': f'Searching for: {search_term}'}
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse({'error': str(e)})

def hello(request):
    return JsonResponse({'message': 'Hello, World! how are you',"r1":"ANup"})
