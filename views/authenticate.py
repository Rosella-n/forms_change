from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from authenticate.models import(User_Info,User,State,Local_Government,Faculty)
import sweetify
from authenticate.forms import LoginForm, SignUpForm
from update_user_signup import (copy_data)
from authenticate.token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings



def signup(request):    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # user=form.cleaned_data['staff_id']          
            user = form.cleaned_data['id_numb']  
            NO_ID_MSG="Sorry, We couldn't Find the User ID {} On Our Database, \
Please contact your staff adviser".format(user).title()

            acct_created_msg='User Account Created,Kindly \
Note That You Must Verify Your Email To Log In'
            
            user_details=User_Info.objects.all().filter(id_numb=user)
           
            if (user_details.exists())==False:
                sweetify.error(request, 'User Details Not Found!', button='Ok', persistent=True,\
                text=NO_ID_MSG)
                                
                form = SignUpForm(request.POST)
            else: 
                userDb_details=User_Info.objects.get(id_numb=user)   

                first_name=userDb_details.first_name
                middle_name=userDb_details.middle_name
                last_name=userDb_details.last_name
                email=userDb_details.email
                display_name='{} {}'.format(userDb_details.first_name,userDb_details.last_name)
                        
                instance=form.save()
                new_user=User.objects.get(id_numb=instance.id_numb)
                User.objects.filter(pk=new_user.pk).update(
                first_name=first_name,middle_name=middle_name,last_name=last_name,\
                email=email,display_name=display_name) 
                # sweetify.info(request, 'Success!', button='Ok', persistent=True, text=acct_created_msg,)     
                
                current_site = get_current_site(request)
                mail_subject = 'Activate Your Account On NACOSS'
                message = render_to_string('registration/account_activation_email.html', {
                    'user': display_name,
                    'domain': current_site.domain,
                    'uid': new_user.pk,
                    'token': account_activation_token.make_token(instance)
                })
                to_email = email
                to_list = [to_email]
                from_email = settings.EMAIL_HOST_USER
                
                send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
                 
                return redirect('activation_sent')
 
    else:
        form = SignUpForm()
 
    return render(request, 'authenticate/signup.html', {'form': form})



def account_activation_sent(request):   
    return render(request, 'registration/account_activation_sent.html', {})

def activate(request, uid, token):
    try:
        user = User.objects.get(pk=uid)
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        
        return render(request, 'registration/account_activation_done.html', {})        
      
    else:
        return render(request,'registration/account_activation_failed.html',{})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            # user=form.cleaned_data['staff_id']          
            user = form.cleaned_data['id_numb']  
        print(form.id_numb)
    else:
        form =LoginForm()
 
    # username = request.POST.get('id_numb')
    # password = request.POST.get('password')
    # print(username)
  
    
    print('not valid')

    return render(request, 'registration/login.html', {'form': form})
    
    

def password_reset(request):   
    return render(request, 'registration/password_reset_form.html', {})

def password_change(request):   
    return render(request, 'registration/password_change_form.html', {})

# def homepage(request):
#     return render(request, 'home.html', {})



