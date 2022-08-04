from django.shortcuts import render,redirect
from .models import Product
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import ReviewForm
from django.contrib import messages
from .models import Product, ReviewRating, ProductGallery

def store(request,category_slug=None):
    if category_slug is None:
        product = Product.objects.filter(is_available=True)
        paginator = Paginator(product,1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        pr_count = product.count()
    else:
        product = Product.objects.filter(category__slug=category_slug,is_available=True)
        paginator = Paginator(product,1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        pr_count = product.count()
    return render(request,'store/store.html',{'products':paged_products,"count":pr_count})


def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    reviews = ReviewRating.objects.filter(product=single_product,status=True)
    product_gallery = ProductGallery.objects.filter(product=single_product)
    context = {
        'single_product': single_product,
        'reviews': reviews,
        'product_gallery': product_gallery,
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    context = {'count':0}
    keyword = request.GET['keyword']
    if keyword:
        try:
            product = Product.objects.order_by('-created_date').filter(Q(product_name__icontains=keyword)|Q(description__icontains=keyword))
            counts = product.count()
            context = {'count':counts,'products':product}
        except:
            pass
    return render(request,'store/store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')#current page
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            #instance to update it not add new 
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')#127.0.0.1
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)