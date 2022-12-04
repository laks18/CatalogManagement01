from django import template
import datetime
from catalogApp.models import Product_Master, Cart
from catalogApp.views import breaklist
from catalogApp.models import *

register = template.Library()

def productimage(data):
    print("My Data is", data)
    product = Product_Master.objects.get(id=data)
    return product.image.url

def productname(data):
    product = Product_Master.objects.get(id=data)
    return product.name

def productprice(data):
    product = Product_Master.objects.get(id=data)
    return product.price

@register.simple_tag
def producttotalprice(data, user):
    product = Product_Master.objects.get(id=data)
    cart = Cart.objects.get(user__user=user)
    qtyli = breaklist(cart.quantity)
    proli = breaklist(cart.productid)
    pindex = proli.index(data)
    qqty = int(qtyli[pindex])
    return qqty*product.price

@register.simple_tag
def ordertotalprice(data, obj):
    product = Product_Master.objects.get(id=data)
    order = Order.objects.get(id=obj)
    qtyli = breaklist(order.quantity)
    proli = breaklist(order.productid)
    pindex = proli.index(data)
    qqty = int(qtyli[pindex])
    return format(qqty*product.price, '.2f')

@register.simple_tag
def productqty(data, user):
    product = Product_Master.objects.get(id=data)
    cart = Cart.objects.get(user__user=user)
    qtyli = breaklist(cart.quantity)
    proli = breaklist(cart.productid)
    pindex = proli.index(data)
    qqty = int(qtyli[pindex])
    return qqty

@register.simple_tag
def orderqty(data, obj):
    product = Product_Master.objects.get(id=data)
    order = Order.objects.get(id=obj)
    qtyli = breaklist(order.quantity)
    proli = breaklist(order.productid)
    pindex = proli.index(data)
    qqty = int(qtyli[pindex])
    return qqty


def iterator(data):
    li = []
    for i in range(1, int(data)+1):
        li.append(i)
    return li

def changeint(data):
    return int(data)


def collectreview(data):
    review = Review.objects.filter(product=data)
    reviewsum = 0
    total = review.count()
    for i in review:
        reviewsum += int(i.ranking)
    avg = reviewsum // total
    return avg


def callproduct(request):
    try:
        cart = Cart.objects.get(user__user=request.user)
        myli = breaklist(cart.productid)
        productid = myli
        # print("My List = ", type(productid), productid)
    except:
        productid = []
    return productid

def lengthfind(request):
    try:
        cart = Cart.objects.get(user__user=request.user)
        myli = breaklist(cart.productid)
        productid = myli
        # print("My List = ", type(productid), productid)
    except:
        productid = []
    lengthpro = len(productid)
    return lengthpro

@register.filter(name="checkodd")
def checkodd(data):
    if data % 2 == 0:
        return True
    else:
        return False
    
@register.filter(name="checklist")   
def checklist(data): 
    data1 = data.split('/')
    lenth = len(data)
    mydata = ''
    myli = ['/vwproduct/','/vwproduct-cateogy/', '/registered-user/', '/orderlist/', '/admin-order-detail/']

    if lenth > 3:
        mydata = "/"+data1[1]+"/"
    else:
        mydata = data
    return (mydata in myli)

@register.filter(name="foot")
def foot(data):
    product = Product_Master.objects.all().order_by('-id')[:6]
    return product
        
register.filter('productimage', productimage)
register.filter('collectreview', collectreview)
register.filter('iterator', iterator)
register.filter('changeint', changeint)
register.filter('productname', productname)
register.filter('productprice', productprice)
register.filter('callproduct',callproduct)
register.filter('lengthfind',lengthfind)
