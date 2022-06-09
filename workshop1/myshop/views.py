

from django.shortcuts import render

from .models import Category, Contact, ImagesProduct, Product

# Create your views here.


def index(request):
    cat = Category.objects.all()
    prod = Product.objects.all()
    img = ImagesProduct.objects.all()
    # print(cat)
    # for i in cat:
    #     print('cat ====>>', i.cat_image)
    return render(request, 'index.html', {'categories': cat, 'prods': prod})


def productspk(request, pk):
    cate = Category.objects.all()
    prods = Product.objects.filter(
        prod_category=pk, prod_status=True).order_by('prod_price')

    return render(request, 'products.html',
                  {'categories': cate, 'products': prods, 'showBread': True})


def products(request):
    cate = Category.objects.all()
    prods = Product.objects.filter(
        prod_recommend=True, prod_status=True).order_by('prod_price')

    return render(request, 'products.html',
                  {'categories': cate, 'products': prods})


def categories(request):
    cate = Category.objects.filter(cat_status=True)
    return render(request, 'categories.html', {'categories': cate})


def product_detail(request, pk):
    # print(pk)
    prod = Product.objects.filter(id=pk).first()

    cate = Category.objects.filter(cat_status=True)
    return render(request, 'product_detail.html', {'categories': cate, 'product': prod, 'showBread': True})


def contact(request):
    sta = False
    if request.POST:
        data = request.POST
        contact = Contact.objects.create(
            firstname=data['fname'],
            lastname=data['fname'],
            e_mail=data['email'],
            message=data['text'],
        )
        contact.save()
        sta = True

    # print(get_recaptcha)
    return render(request, 'contact.html', {'showBread': True, 'sta': sta})
