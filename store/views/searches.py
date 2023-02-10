from django.shortcuts import render, redirect, HttpResponse
# from django.views import View
# from store.models.product import Products
from store.models.product import Products




# class Search(View):
#     def searches(self, request):
#         return HttpResponse('This is search')

def searches(request):
    query = request.GET['query']
    products = Products.objects.filter(name__icontains = query)
    params = {'products': products}
    # print(allPosts)
    return render(request, 'searches.html',params)
    # return HttpResponse('This will work')
