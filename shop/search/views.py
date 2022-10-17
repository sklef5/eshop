from django.db.models import Q
from django.shortcuts import render

from product.models import ProductModel

def search(request):
    query = request.GET.get('q')
    if not query:
        mes = 'Введіть данні для пошуку'
        return render(request, 'main/message_list.html', {'form': mes})
    else:
        search_list = ProductModel.objects.filter(
        Q(slug__icontains=query) | Q(description__icontains=query)|Q(name__icontains=query)
        )
        return render(request,'search/search.html', {'object_list': search_list})
