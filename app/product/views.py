from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_POST

from product.models import Product


def index(request):
    product = Product.objects.first()
    return render(request, 'index.html', {'product': product})


@login_required
@require_POST
def order_success_view(request):
    imp_uid = request.POST.get('imp_uid')
    print(request.POST)
    print(request)
    return render(request, 'payment_success.html', {'imp_uid', imp_uid})
