from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from . forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
# Create your views here.

# @login_required
# @cache_page(60*10)
@vary_on_headers("User-Agent")
def index(request):
    #getting items from the database
    item_list = Item.objects.all()
    paginator = Paginator(item_list,5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # creating context
    context = {
        "page_obj":page_obj
    }
    return render(request,'myapp/index.html',context)

# class Index(ListView):
#     model = Item
#     template_name = 'myapp/index.html'
#     context_object_name = 'item_list'

# def detail(request,id):
#     item = Item.objects.get(id=id)
#     context2 = {
#         "item":item
#     }
#     return render(request,"myapp/detail.html",context2)

class Detail(DetailView):
    model = Item
    template_name = "myapp/detail.html"
    context_object_name = 'item'

# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if request.method == "POST":
#         print("Post request is triggered")
        
#         if form.is_valid():
#             form.save()
#             return redirect('myapp:index')
#     context3 = {
#         "form" : form
#     }
#     return render(request,'myapp/item-form.html',context3)


class CreateItem(CreateView):
    model = Item
    fields = ['food_name','food_desc','food_price','food_image']
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

# def edit(request,id):
#     item  = Item.objects.get(id = id)
#     form = ItemForm(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect('myapp:index')
#     context ={
#         "form":form
#     }
#     return render(request,'myapp/item-form.html',context)

class Edit(UpdateView):
    model = Item
    fields = ['food_name','food_desc','food_price','food_image']
    def get_queryset(self):
        return Item.objects.filter(user_name=self.request.user) 


# def delete(request,id):
#     item = Item.objects.get(id = id)
#     if request.method == "POST":
#         item.delete()
#         return redirect('myapp:index')
#     return render(request,'myapp/delete.html')


class Delete(DeleteView):
    model = Item
    template_name_suffix = '_delete'
    success_url = reverse_lazy('myapp:index')
    def get_queryset(self):
        return Item.objects.filter(user_name=self.request.user) 