from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Service
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse

@login_required(login_url='/authentication/login')
def index(request):
    categories = Category.objects.all()
    services = Service.objects.all()

    paginator = Paginator(services,3)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
        'categories': categories,
        'services': services,
        'page_obj': page_obj
    }
    return render(request, 'services/index.html', context)

@login_required(login_url='/authentication/login')
def add_service(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST  # Send back the form data in case of an error
    }

    if request.method == "GET":
        return render(request, 'services/add_services.html', context)

    if request.method == "POST":
        cost = request.POST.get('cost')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        date = request.POST.get('date')

        # Validate form inputs
        if not cost:
            messages.warning(request, 'Please enter cost')
            return render(request, 'services/add_services.html', context)

        if not description:
            messages.warning(request, 'Please enter description')
            return render(request, 'services/add_services.html', context)

        if not category_id:
            messages.warning(request, 'Please select a category')
            return render(request, 'services/add_services.html', context)

        if not date:
            messages.warning(request, 'Please enter a date')
            return render(request, 'services/add_services.html', context)

        

        # Ensure that the category is fetched from the database
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, 'Invalid category selected')
            return render(request, 'services/add_services.html', context)

        # Create the service object
        Service.objects.create(owner=request.user, cost=cost, date=date, category=category, description=description)
        messages.success(request, 'Service saved successfully')

        return redirect('services')
    
def edit_service(request, id):
    service = Service.objects.get(pk = id)
    categories = Category.objects.all()
    context={
        'service': service,
        'values': service,
        'categories': categories
    }
    if request.method=='GET':
        return render(request, 'services/edit_service.html', context)
    if request.method == "POST":
        cost = request.POST.get('cost')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        date = request.POST.get('date')

        # Validate form inputs
        if not cost:
            messages.warning(request, 'Please enter cost')
            return render(request, 'services/edit_services.html', context)

        if not description:
            messages.warning(request, 'Please enter description')
            return render(request, 'services/edit_service.html', context)

        if not category_id:
            messages.warning(request, 'Please select a category')
            return render(request, 'services/edit_service.html', context)

        if not date:
            messages.warning(request, 'Please enter a date')
            return render(request, 'services/edit_service.html', context)

        

        # Ensure that the category is fetched from the database
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, 'Invalid category selected')
            return render(request, 'services/edit_service.html', context)
        
        service.owner = request.user
        service.cost = cost
        service.date = date
        service.description = description
        service.category = category.name

        service.save()
        messages.success(request, 'Service updated successfully')

        return redirect('services')
    
def service_delete(request, id):
    service = Service.objects.get(pk = id)
    service.delete()
    messages.success(request, 'Service deleted successfully')
    return redirect('services')
    
def reports_plots(request):
    services = Service.objects.filter(date__year=2024)
    final_report = {}
    
    def get_category(service):
        return service.category
    
    category_list = list(set(map(get_category,services)))

    def get_category_cost(category):
        cost = 0
        filter_by_category = services.filter(category=category)
        cost = sum(service.cost for service in filter_by_category)
        return cost

    for x in services:
        for y in category_list:
            final_report[y] = get_category_cost(y)

    return JsonResponse({'category_report': final_report}, safe=False)

def stats_view(request):
    return render(request, 'services/stats.html')