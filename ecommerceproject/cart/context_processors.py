from .models import Cart,CartItem
from .views import _cart_id

def counter(request):
    item_counter=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            cart_items=CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_counter += cart_item.quantity
        except Cart.DoesNotExist:
            item_counter = 0
        return dict(item_counter=item_counter)
