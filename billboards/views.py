from django.shortcuts import render, redirect, get_object_or_404
from .models import Billboard, Company, Payment
from django.http import JsonResponse
from django.conf import settings


def dashboard(request):
    # Get query parameters for filtering
    location_query = request.GET.get('location', '')
    company_query = request.GET.get('company', '')
    payment_status = request.GET.get('payment_status', '')

    # Filter Billboards
    billboards = Billboard.objects.all()

    if location_query:
        billboards = billboards.filter(location__icontains=location_query)

    if company_query:
        billboards = billboards.filter(rented_by__name__icontains=company_query)

    if payment_status:
        if payment_status.lower() == 'paid':
            billboards = billboards.filter(is_paid=True)
        elif payment_status.lower() == 'unpaid':
            billboards = billboards.filter(is_paid=False)

    # Get all companies for filtering dropdown
    companies = Company.objects.all()

    return render(request, 'billboards/dashboard.html', {
        'billboards': billboards,
        'companies': companies,
        'location_query': location_query,
        'company_query': company_query,
        'payment_status': payment_status,
    })

def add_coordinates(request, billboard_id):
    """
    Handle the addition or update of geographical coordinates for a billboard.
    """
    billboard = get_object_or_404(Billboard, pk=billboard_id)

    if request.method == 'POST':
        coordinates = request.POST.get('coordinates')
        if coordinates:
            billboard.coordinates = coordinates
            billboard.save()
            return redirect('dashboard')

    return render(request, 'billboards/add_coordinates.html', {'billboard': billboard})


def payment_form(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        # Simulate payment gateway integration
        amount = request.POST.get('amount')
        transaction_id = request.POST.get('transaction_id')

        # Save payment
        payment = Payment.objects.create(
            company=company,
            amount=amount,
            transaction_id=transaction_id,
        )

        # Update billboards for the company to "Paid"
        company_billboards = Billboard.objects.filter(rented_by=company)
        company_billboards.update(is_paid=True)

        return redirect('dashboard')

    return render(request, 'billboards/payment_form.html', {'company': company})


def mark_paid(request, billboard_id):
    billboard = get_object_or_404(Billboard, pk=billboard_id)
    billboard.is_paid = True
    billboard.save()
    return JsonResponse({'status': 'success'})
