from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):

    return "₨"+str(number)

@register.filter(name='multiply')
def multiply(item,qty):
    total_price=item*qty
    return total_price

