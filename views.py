from django.shortcuts import render,redirect
from Cabin.models import Cabin_Img1,Cabin_Img2,Cabin_Img3,Cabin_Img4
from conference.models import Conference_Img1,Conference_Img2,Conference_Img3,Conference_Img4
from breakroom.models import Breakroom_Img1,Breakroom_Img2,Breakroom_Img3,Breakroom_Img4
from reception.models import Reception_Img1,Reception_Img2,Reception_Img3,Reception_Img4
from kitchen.models import Kitchen_Img1,Kitchen_Img2,Kitchen_Img3,Kitchen_Img4,Kitchen_Img5,Kitchen_Img6,Kitchen_Img7
from livingroom.models import Livingroom_Img1,Livingroom_Img2,Livingroom_Img3,Livingroom_Img4,Livingroom_Img5,Livingroom_Img6,Livingroom_Img7
from bathroom.models import Bathroom_Img1,Bathroom_Img2,Bathroom_Img3,Bathroom_Img4,Bathroom_Img5,Bathroom_Img6,Bathroom_Img7
from bedroom.models import Bedroom_Img1,Bedroom_Img2,Bedroom_Img3,Bedroom_Img4,Bedroom_Img5,Bedroom_Img6,Bedroom_Img7
from residential.models import Residential_Img1,Residential_Img2,Residential_Img3,Residential_Img4,Residential_Img5
from commercial.models import Commercial_Img1,Commercial_Img2,Commercial_Img3,Commercial_Img4,Commercial_Img5
from about.models import Aboutimage1,Aboutimage2
from services.models import Servicesimage1
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from feedback.models import Feedback
from reachoutform.models import ReachoutForm, Picture


  






def services(request):
    servicesimage1=Servicesimage1.objects.all()
    
    SERVICES={ 
    'servicesimage1':servicesimage1,
    }
    return render(request,'services.html',SERVICES)

def display(request):
     return render(request,'display.html')


def cabin_gallery(request):
    cabin01=Cabin_Img1.objects.all()
    cabin02=Cabin_Img2.objects.all()
    cabin03=Cabin_Img3.objects.all()
    cabin04=Cabin_Img4.objects.all()
    CABIN={
       'cabin01':cabin01,
       'cabin02':cabin02,
       'cabin03':cabin03,
       'cabin04':cabin04,
    }
    return render(request,'cabin.html',CABIN)

def conference_gallery(request):
    conference01=Conference_Img1.objects.all()
    conference02=Conference_Img2.objects.all()
    conference03=Conference_Img3.objects.all()
    conference04=Conference_Img4.objects.all()
    CONFERENCE={
       'conference01':conference01,
       'conference02':conference02,
       'conference03':conference03,
       'conference04':conference04,
    }
    return render(request,'conferencerm.html',CONFERENCE)

def breakroom_gallery(request):
    breakroom01=Breakroom_Img1.objects.all() 
    breakroom02=Breakroom_Img2.objects.all()
    breakroom03=Breakroom_Img3.objects.all()
    breakroom04=Breakroom_Img4.objects.all()
    BREAKROOM={
       'breakroom01':breakroom01,
       'breakroom02':breakroom02,
       'breakroom03':breakroom03,
       'breakroom04':breakroom04,
    }
    return render(request,'breakroom.html',BREAKROOM)


def reception_gallery(request):
    reception01=Reception_Img1.objects.all() 
    reception02=Reception_Img2.objects.all()
    reception03=Reception_Img3.objects.all()
    reception04=Reception_Img4.objects.all()
    RECEPTION={
       'reception01':reception01,
       'reception02':reception02,
       'reception03':reception03,
       'reception04':reception04,
    }
    return render(request,'reception.html',RECEPTION)


def kitchen_gallery(request):
    kitchen01=Kitchen_Img1.objects.all()
    kitchen02=Kitchen_Img2.objects.all()
    kitchen03=Kitchen_Img3.objects.all()
    kitchen04=Kitchen_Img4.objects.all()
    kitchen05=Kitchen_Img5.objects.all()
    kitchen06=Kitchen_Img6.objects.all()
    kitchen07=Kitchen_Img7.objects.all()
    KITCHEN={
       'kitchen01':kitchen01,
       'kitchen02':kitchen02,
       'kitchen03':kitchen03,
       'kitchen04':kitchen04,
       'kitchen05':kitchen05,
       'kitchen06':kitchen06,
       'kitchen07':kitchen07,
    }
    return render(request,'kitchen.html',KITCHEN)

def livingroom_gallery(request):
    livingroom01=Livingroom_Img1.objects.all()
    livingroom02=Livingroom_Img2.objects.all()
    livingroom03=Livingroom_Img3.objects.all()
    livingroom04=Livingroom_Img4.objects.all()
    livingroom05=Livingroom_Img5.objects.all()
    livingroom06=Livingroom_Img6.objects.all()
    livingroom07=Livingroom_Img7.objects.all()
    LIVINGROOM={
       'livingroom01':livingroom01,
       'livingroom02':livingroom02,
       'livingroom03':livingroom03,
       'livingroom04':livingroom04,
       'livingroom05':livingroom05,
       'livingroom06':livingroom06,
       'livingroom07':livingroom07,
    }
    return render(request,'livingroom.html',LIVINGROOM)

def bathroom_gallery(request):
    bathroom01=Bathroom_Img1.objects.all()
    bathroom02=Bathroom_Img2.objects.all()
    bathroom03=Bathroom_Img3.objects.all()
    bathroom04=Bathroom_Img4.objects.all()
    bathroom05=Bathroom_Img5.objects.all()
    bathroom06=Bathroom_Img6.objects.all()
    bathroom07=Bathroom_Img7.objects.all()
    BATHROOM={
       'bathroom01':bathroom01,
       'bathroom02':bathroom02,
       'bathroom03':bathroom03,
       'bathroom04':bathroom04,
       'bathroom05':bathroom05,
       'bathroom06':bathroom06,
       'bathroom07':bathroom07,
    }
    return render(request,'bathroom.html',BATHROOM)


def bedroom_gallery(request):
    bedroom01=Bedroom_Img1.objects.all()
    bedroom02=Bedroom_Img2.objects.all()
    bedroom03=Bedroom_Img3.objects.all()
    bedroom04=Bedroom_Img4.objects.all()
    bedroom05=Bedroom_Img5.objects.all()
    bedroom06=Bedroom_Img6.objects.all()
    bedroom07=Bedroom_Img7.objects.all()
    BEDROOM={
       'bedroom01':bedroom01,
       'bedroom02':bedroom02,
       'bedroom03':bedroom03,
       'bedroom04':bedroom04,
       'bedroom05':bedroom05,
       'bedroom06':bedroom06,
       'bedroom07':bedroom07,
    }
    return render(request,'bedroom.html',BEDROOM)

def residential_gallery(request):
    residential01=Residential_Img1.objects.all()
    residential02=Residential_Img2.objects.all()
    residential03=Residential_Img3.objects.all()
    residential04=Residential_Img4.objects.all()
    residential05=Residential_Img5.objects.all()
  
    RESIDENTIAL={
       'residential01':residential01,
       'residential02':residential02,
       'residential03':residential03,
       'residential04':residential04,
       'residential05':residential05,
       
    }
    return render(request,'residential.html',RESIDENTIAL)

def commercial_gallery(request):
    commercial01=Commercial_Img1.objects.all()
    commercial02=Commercial_Img2.objects.all()
    commercial03=Commercial_Img3.objects.all()
    commercial04=Commercial_Img4.objects.all()
    commercial05=Commercial_Img5.objects.all()
  
    COMMERCIAL={
       'commercial01':commercial01,
       'commercial02':commercial02,
       'commercial03':commercial03,
       'commercial04':commercial04,
       'commercial05':commercial05,
       
    }
    return render(request,'commercial.html',COMMERCIAL)

# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password')
#         pass2=request.POST.get('confirm-password')

#         if pass1!=pass2:
#             return HttpResponse("Your password and confirm password are not same !")
#         else:
#          my_user=User.objects.create_user(uname,email,pass1)
#          my_user.save()
#          return redirect('login')

#     return render (request,'signupdemo.html')
  
def LoginPage(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         user=authenticate(request,username=username,password=password)
         if user is not None:
             login(request,user)
             return redirect('design_form')
         else:
             return HttpResponse("Username or password is incorrect")
    return render(request,'logindemo.html')



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Function to send an email using smtplib
def send_email(to_email, first_name, subject, message_body):
    sender_email = "delreydecors011@gmail.com"
    sender_password = "vpze hzpn crmj rryf"

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(message_body, "plain"))

    try:
        # Connect to Gmail's SMTP server and send the email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Signup view
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm-password')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            # Create a new user
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()

            # Send email after signup
            subject = "Welcome to Del Rey Decors"
            message_body = f"Hello {uname},\n\nYou have successfully signed up for Del Rey Decors. Thank you for joining us!"
            send_email(email, uname, subject, message_body)

            return redirect('login')
    return render(request, 'signupdemo.html')

# Login view
# def LoginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)

#             # Send email after login
#             subject = "Login Notification"
#             message_body = f"Hello {user.username},\n\nYou have successfully logged in to Del Rey Decors. Welcome back!"
#             send_email(user.email, user.username, subject, message_body)

#             return redirect('design_form')  # Redirect to the design form page
#         else:
#             return HttpResponse("Username or password is incorrect")
#     return render(request, 'logindemo.html')



def About(request):
    aboutimage1=Aboutimage1.objects.all()
    aboutimage2=Aboutimage2.objects.all()

    ABOUT={ 
    'aboutimage1':aboutimage1,
    'aboutimage2':aboutimage2,
     

    }
    return render(request,'about1.html',ABOUT)
        


# views.py



def submit_feedback(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        message = request.POST.get('message')

        # Save feedback to the database
        Feedback.objects.create(email=email, rating=rating, message=message)
        return redirect('submit_feedback')  # Stay on the form page
    
    # return HttpResponse(f"Thank you for your feedback!")

    return render(request, 'display.html')




# views.py in reachoutform app
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
from django.core.files.storage import default_storage
import base64


# Function to generate PDF using xhtml2pdf
def generate_pdf(form_data, images):
    # Create a string from the HTML template and form data
    html_string = render_to_string('pdf_template.html', {
        'form_data': form_data,
        'images': images
    })

    # Create a PDF file in memory
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_string.encode('UTF-8')), result)

    if not pdf.err:
        return result.getvalue()
    return None

# Function to send an email with the PDF attachment
def send_email_with_pdf(to_email, first_name, last_name, pdf_data):
    # Define email parameters
    subject = "Form Submission Details"
    sender_email = "delreydecors011@gmail.com"
    sender_password = "vpze hzpn crmj rryf"

    # Create the email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    body = f"Hello {first_name} {last_name},\n\nPlease find attached the details of your form submission."
    message.attach(MIMEText(body, "plain"))

    # Attach the PDF
    if pdf_data:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(pdf_data)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="form_submission.pdf"')
        message.attach(part)

    try:
        # Set up the server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# View function to handle form submission
@login_required
def reachout_form_view(request):
    if request.method == 'POST':
        # Get the form details
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment_mode = request.POST.get('paymentMode')

        # Get selected spaces and services
        selected_spaces = ', '.join(request.POST.getlist('space'))
        selected_services = ', '.join(request.POST.getlist('service'))
        total_cost = float(request.POST.get('totalCost', 0))

        # Create a new ReachoutForm object and save it to the database
        submission = ReachoutForm.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            spaces=selected_spaces,
            services=selected_services,
            total_cost=total_cost,
            payment_mode=payment_mode,
        )

        # Handle image uploads
        images = request.FILES.getlist('photoInput')
        image_data = []
        for image in images:
            # Save the image in the Picture model
            picture = Picture.objects.create(reachout_form=submission, image=image)

            # Convert the image to base64
            image_path = picture.image.path
            with default_storage.open(image_path, 'rb') as img_file:
                img_data = img_file.read()
                encoded_img = base64.b64encode(img_data).decode('utf-8')
                image_data.append({
                    'name': picture.image.name,
                    'content': encoded_img
                })

        # Prepare PDF content
        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'spaces': selected_spaces,
            'services': selected_services,
            'total_cost': total_cost,
            'payment_mode': payment_mode,
        }
        pdf_data = generate_pdf(form_data, image_data)

        # Send the email with the PDF
        send_email_with_pdf(email, first_name, last_name, pdf_data)

        return HttpResponse('Form submitted successfully. Check your email for further details.')

    return render(request, 'comform.html')
