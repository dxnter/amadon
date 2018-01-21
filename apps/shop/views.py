from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'total_spent' not in request.session:
        request.session['total_spent'] = 0
    if 'products_ordered' not in request.session:
        request.session['products_ordered'] = 0
    return render(request, 'shop/index.html')

def checkout(request):
    checkout_product_id = request.POST.get('product_id')
    request.session['checkout_quantity'] = int(request.POST.get('quantity'))

    product_prices = [{'1': 19.99}, {'2': 29.99}, {'3': 4.99}, {'4': 49.99}]
    for product in product_prices:
        for product_id in product:
            if checkout_product_id == product_id:
                request.session['product_price'] = (product[product_id] * request.session['checkout_quantity'])
                request.session['total_spent'] += (product[product_id] * request.session['checkout_quantity'])
                request.session['products_ordered'] += request.session['checkout_quantity']
    
    product_names = [{'1': 'Dojo Tshirt'}, {'2': 'Dojo Sweater'}, {'3': 'Dojo Cup'}, {'4': 'Algorithm Book'}]
    for product in product_names:
        for product_name in product:
            if checkout_product_id == product_name:
                request.session['product_name'] = product[product_name]

    return redirect('/success')

def success(request):
    return render(request, 'shop/success.html')