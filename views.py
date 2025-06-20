from django.shortcuts import render
from residentialform.models import ResidentialFormSubmission, Picture
from django.http import HttpResponse

# Create your views here.



def residential_form_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment_mode = request.POST.get('payment_mode')

        total_cost = 0
        selected_spaces = request.POST.getlist('selected_spaces')
        for space in selected_spaces:
            if space == "Living Room":
                total_cost += 200000
            elif space == "Kitchen":
                total_cost += 150000
            elif space == "Bedroom":
                total_cost += 300000
            elif space == "Bathroom":
                total_cost += 100000

        selected_services = request.POST.getlist('selected_services')
        for service in selected_services:
            total_cost += 50000

        submission = ResidentialFormSubmission.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            total_cost=total_cost,
            payment_mode=payment_mode,
            selected_spaces=', '.join(selected_spaces),
            selected_services=', '.join(selected_services)
        )

        # Handle image uploads
        images = request.FILES.getlist('images')
        for image in images:
            Picture.objects.create(submission=submission, image=image)

        return HttpResponse('Form submitted successfully')

    return render(request, 'resform.html')

