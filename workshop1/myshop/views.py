from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings


from .models import Category, Contact, Product
from .form import FormWithCaptcha

import requests

from django.contrib.auth import login, logout
# Create your views here.


def index(request):
    cat = Category.objects.all()
    prod = Product.objects.all()
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
    prod_rec = Product.objects.filter(prod_recommend=True)

    cate = Category.objects.filter(cat_status=True)
    return render(request, 'product_detail.html', {'categories': cate, 'product': prod, 'prods_rec': prod_rec, 'showBread': True})


def contact(request):
    sta = False
    capcha = FormWithCaptcha()
    if request.POST:
        # print('Post ===>>> ', request.POST.get("g-recaptcha-response"))
        recap = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': request.POST.get("g-recaptcha-response")
            })
        print(recap.json())
        if recap.json()['success']:
            data = request.POST
            contact = Contact.objects.create(
                firstname=data['fname'],
                lastname=data['fname'],
                e_mail=data['email'],
                message=data['text'],
            )
            contact.save()
            sta = True
        else:
            messages.error(request, 'Save Failed')
    # print(get_recaptcha)
    return render(request, 'contact.html', {'showBread': True, 'sta': sta, 'capcha': capcha})

# def contact_new(request):
#     category = Category.objects.filter(published=True)
#     form = ContactForm()
#     if  request.method == 'POST':
#         respon = request.POST.get('g-recaptcha-response')
#         googlerecap = {
#             'secret':'6LfQWzQbAAAAAEJLOBBfDZ9YOBy_Z4NGF9Rt6oHJ',
#             'response':respon
#         }
#         recap = requests.post('https://www.google.com/recaptcha/api/siteverify', googlerecap)
#         if recap.json()['success']:
#             form = ContactForm(request.POST, request.FILES)
#             if form.is_valid():
#                 contact = form.save(commit=False)
#                 contact.published = True
#                 contact.save()
#                 form.save_m2m()
#                 messages.success(request, 'Save success')
#                 return HttpResponseRedirect(reverse('contact', kwargs={} ))
#         else:
#             messages.error(request, 'Save Failed')
#     return render(request, 'page/contact.html',{
#         'form': form,
#         'category':category
#     })


def login_or_regis_view(req):
    formRegis = UserCreationForm()
    formLogin = AuthenticationForm()

    if req.POST:
        if req.POST['form'] == 'regis':
            formRegis = UserCreationForm(req.POST)
            if formRegis.is_valid:
                user = formRegis.save()
                login(req, user)
                return redirect('products')
        if req.POST['form'] == 'login':
            formLogin = AuthenticationForm(data=req.POST)
            if formLogin.is_valid():
                user = formLogin.get_user()
                login(req, user)
                return redirect('products')

    return render(req, 'signinup.html', {'regis': formRegis, 'login': formLogin, 'categories': Category.objects.all()})


def logout_view(req):
    # if req.method == 'POST':
    logout(req)
    return redirect('products')
