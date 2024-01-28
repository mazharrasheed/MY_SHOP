from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):

    keys=cart.keys()
    for id  in keys:
        if int(id)==product.id:
            return True
    return False

@register.filter(name='product_qty_incart')
def product_qty_incart(product,cart):

    keys=cart.keys()
    for id  in keys:
        if int(id)==product.id:
            return cart.get(id)
    return False

@register.filter(name='pro_Total_Price')
def pro_Total_Price(product,cart):

    total_price=product.pro_price*product_qty_incart(product,cart)
    return total_price

@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum=0
    for p in products:
        sum+=pro_Total_Price(p,cart)
    return sum




