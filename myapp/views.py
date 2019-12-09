import logging
from django.shortcuts import render
from .models import Shop, Product
from django.shortcuts import get_object_or_404
from .forms import ShopForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse, reverse_lazy

logger = logging.getLogger(__name__)  ## shop.views


def shop_list(request):
    qs = Shop.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(거래처명__icontains=q) #대소문자를 구별하지 않겠다.
    logger.debug('query : {}'.format(q)) 
    return render(request, 'myapp/shop_list.html', {
        'shop_list':qs,
        'q' : q,
    })

def shop_detail(request,pk):
    shop = get_object_or_404(Shop, 거래처코드=pk)
    logger.debug('query : {}'.format(shop)) 
    return render(request, 'myapp/shop_detail.html', {
        'shop':shop,
    })

class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm
    template_name = 'myapp/shop_form.html'

    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(self.request, '새 글을 저장했습니다.')
        return res

shop_new = ShopCreateView.as_view()

class ShopUpdateView(UpdateView):
    model=Shop
    form_class = ShopForm

shop_edit = ShopUpdateView.as_view()

class ShopDeleteView(DeleteView):
    model = Shop
    def get_success_url(self):
        return reverse('myapp:shop_list')

shop_delete = ShopDeleteView.as_view()




##########################
from django.shortcuts import render
from .filters import ShopFilter

def search(request):
    Shop_list = Shop.objects.all()
    print('---------------',Shop_list)
    Shop_filter = ShopFilter(request.GET, queryset=Shop_list)
    print(Shop_filter)
    return render(request, 'myapp/shop_list_filter.html', {'filter': Shop_filter})