from django import template
# Code taken and adapted from Boutique Ado walkthrough project
# To calculate subtotal in bag for each line item


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity