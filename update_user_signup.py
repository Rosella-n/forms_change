
from authenticate.models import (User,User_Info)
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from authenticate.token import account_activation_token
from django.template.loader import render_to_string
from django.conf import settings
# def signup(request):    
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.cleaned_data['staff_id']          
           
#             NO_ID_MSG="Sorry, We couldn't Find the Staff ID {} On Our Database, \
# Please contact AdminHr".format(user).title()

#             acct_created_msg='User Account Created,Kindly \
# Note That You Must Verify Your Email To Log In'
           
#             user_details=AllStaff.objects.all().filter(staff_id=user)
           
#             if (user_details.exists())==False:
#                 sweetify.error(request, 'User Details Not Found!', button='Ok', persistent=True,\
#                 text=NO_ID_MSG)
                               
#                 form = CustomUserCreationForm(request.POST)
#             else:
                                         
#                 sweetify.info(request, 'Success!', button='Ok', persistent=True, text=acct_created_msg,)        
#                 instance=form.save()
#                 update_new_user_details(request,user)
#                 Log_msg="Signed Up For A New Account"
#                 new_user=User.objects.get(staff_id=user)
#                 Activity_Log.objects.create(created_by=new_user,description=Log_msg)

#                 current_site = get_current_site(request)
#                 mail_subject = 'ICT DocuScan: Activate Your Account.'
#                 message = render_to_string('registration/account_activation_email.html', {
#                     'user': instance.display_name,
#                     'domain': current_site.domain,
#                     'uid': instance.staff_id,
#                     'token': account_activation_token.make_token(instance)
#                 })
#                 to_email = form.cleaned_data.get('email')
#                 to_list = [to_email]
#                 from_email = settings.EMAIL_HOST_USER
               
#                 send_mail(mail_subject, message, from_email, to_list, fail_silently=True)

#                 return redirect('activation_sent')
 
#     else:
#         form = CustomUserCreationForm()
 
#     return render(request, 'registration/signup.html', {'form': form})

def copy_data(request,numb_id):    
    user_data=User_Info.objects.get(id_numb=numb_id)
    instance=User.objects.create(pk=user_data.pk,email=user_data.email,display_name=user_data,\
    first_name=user_data.first_name,middle_name=user_data.middle_name,last_name=user_data.last_name,\
    phone=user_data.phone,) 
    # print(instance)
    
#     user_data=User_Info.objects.get(id_numb=numb_id)
#     user_email=user_data.email
#     current_site = get_current_site(request)
#     mail_subject = 'Activate Your Account On NACOSS '
#     message = render_to_string('registration/account_activation_email.html', {
#                     'user': user_data.first_name,
#                     'domain': current_site.domain,
#                     'uid': user_data.pk,
#                     'token': account_activation_token.make_token(instance)
#                 })
    
#     to_list = [user_email]
#     from_email = settings.EMAIL_HOST_USER
    
#     send_mail(mail_subject, message, from_email, to_list, fail_silently=True)




# def email_link(request,numb_id):
#     user_data=User_Info.objects.get(id_numb=numb_id)
#     user_email=user_data.email
#     current_site = get_current_site(request)
#     mail_subject = 'Activate Your Account On NACOSS '
#     message = render_to_string('registration/account_activation_email.html', {
#                     'user': user_data.first_name,
#                     'domain': current_site.domain,
#                     'uid': user_data.id_numb,
#                     'token': account_activation_token.make_token(user_data)
#                 })
    
#     to_list = [user_email]
#     from_email = settings.EMAIL_HOST_USER
    
#     send_mail(mail_subject, message, from_email, to_list, fail_silently=True)


   