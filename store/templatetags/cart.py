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
