import logging
from django.shortcuts import render
from .models import Shop, Product
from django.shortcuts import get_object_or_404
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