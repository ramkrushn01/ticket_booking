from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from ticket_booking.models import RequistOtpAuth, BookSeat, UserSavedMessages
from django.contrib.auth.decorators import login_required
import smtplib
from random import randint
import json
import email.message

componyInfo = {
    'username':'Enter Your Gmail Here',
    'password':'Enter Your Gmail Password Here'
}

# Create your views here.
def sendEmailtoUser(useremail,subject,msgContent):
    try:
        msgSend = email.message.Message()
        msgSend['Subject'] = subject
        msgSend['From'] = componyInfo['username']
        msgSend['To'] = useremail
        msgSend.add_header ('Content-Type','text/html')
        msgSend.set_payload(msgContent)

        sMail = smtplib.SMTP('smtp.gmail.com', 587)
        sMail.starttls()
        sMail.login(componyInfo['username'], componyInfo['password'])
        # massage = f'Subject:{subject}\n\n{msgContent}'
        sMail.sendmail(from_addr='salunkhe9307@gmail.com',
                       to_addrs=useremail, msg=msgSend.as_string())
        sMail.quit()

        return True
    except:
        return False

def myAllBooking_rest(request):
    try:
        username = request
        mybook = BookSeat.objects.filter(username=username)
        mblist = []
        for myb in mybook.values_list():
            mblist.append(list(myb))

        return mblist
    except:
        content = {
            'nby':'Not Booking Yet'
        }
        return 'Not Booking Yet'
        

def test(request):
    pass
    # print(request.user)
    # with open('test.json', '+w') as file:
        # json.dump(dict(rest),file)
        # file.write(str(rest))

    # return render(request, 'test.html',{'rest':str(rest)})
    # return render(request,'test.html')



def home(request):
    if request.user.is_anonymous:
        loginUser = 'login'
        loginyes = ''
        content = {'loginyes': loginyes}

    else:
        loginUser = request.user
        loginyes = 'Logout'
        book_now = request.user
        book_table_value = myAllBooking_rest(request.user)
        content = {'loginUser': loginUser, 'loginyes': loginyes,'book_now':book_now,'book_table_value':book_table_value}
    
    # messages.add_message(request,messages.INFO,'login successful!')
    # messages.success(request,'Login Successful!')
    
    return render(request, 'home.html', content)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            # return JsonResponse({'success':'Login Success','userName':user.username})
            messages.success(request,'Login Successful!')

            return redirect('/')
        else:
            messages.error(request,'Login Unsuccessful Please Try again')
            return redirect('/')
            return JsonResponse({'error': 'Check Username or Password'})
    else:
        messages.error(request,'Login Unsuccessfull Please Try again')

        return redirect('/')



def logoutUser(request):
    logout(request)
    messages.success(request,'Logout Successful!')
    return redirect('/')


def sendOtp(request):
    # return JsonResponse(request['post_data'])

    if request.method == 'GET':
        name = request.GET.get('name')
        userEmail = request.GET.get('username')
        password = request.GET.get('password')
        # print('*********************************************************************************************')
        # print(name,userEmail,password)

        otpCreate = randint(10001, 99999)
        
        sendEmailContent = f"""
<html>
  
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     
   <title>Email From Travel</title>
</head>
  
<body>


<h1> <span style="color: #ffa500;">T</span>RAVEL</h1><br><br>

<p>
    To verify your email address, please use the following One Time Password (OTP): <br>
    <h2><b>{otpCreate}</b></h2>
    <br>
    Do not share this <b>OTP with anyone.</b> Travel takes your account security very seriously.
</p>

<br>
<br>
<br>
<br><br><br>
<p>
    <b>Thank You!</b><br>
    Team <span style="color: #ffa500;">T</span>ravel
</p>


</body>
</html>

"""
        subjectUser = 'OTP From Travel'

        try:
            snd = sendEmailtoUser(userEmail,subjectUser,sendEmailContent)
            if snd:                    
                saveOtp = RequistOtpAuth()
                saveOtp.username = userEmail
                saveOtp.otp = otpCreate
                saveOtp.save()

                content = {'name': name,
                           'username': userEmail,
                           'password': password}

                return JsonResponse(content)

        except Exception as err:
            contenterr = {
                'error': 'Check Your Email'
            }

            return JsonResponse(contenterr)

    elif request.method == '':
        content = {
            'ramkrusn': 'salunkhe',
            'manoj': 'bhosale'
        }

        return JsonResponse(content)


def signUpUser(request):

    if request.method == 'GET':
        name = request.GET.get('name')
        userEmail = request.GET.get('username')
        password = request.GET.get('password')
        otp = request.GET.get('otp')
        if RequistOtpAuth.objects.filter(username=userEmail, otp=otp):
            try:
                user = User.objects.create_user(name, userEmail, password)

                user.save()
                login(request, user)
                rqstUser = RequistOtpAuth.objects.filter(
                    username=userEmail, otp=otp)
                rqstUser.delete()
                content = {
                    'success': 'Login Successful!',
                    'userName': user.username
                }
                return JsonResponse(content)
            except Exception as err:
                content = {
                    'error': 'Incorrect OTP'
                }

                return JsonResponse(content)
        else:
            content = {
                'error': 'Incorrect OTP'
            }

            return JsonResponse(content)


@login_required(login_url='/')
def bookNow(request):

    if request.method == 'POST':
        username = request.user 
        userEmail = User.objects.get(username=request.user).email
        whereTo = request.POST.get('where-to')
        howMany = request.POST.get('how-many')
        arrivals = request.POST.get('arrivals')
        leaving = request.POST.get('leaving')

        saveBooking = BookSeat()
        saveBooking.username = username
        saveBooking.userEmail = userEmail
        saveBooking.whereTo = whereTo
        saveBooking.howMany = howMany
        saveBooking.arrivals = arrivals
        saveBooking.leaving = leaving

        saveBooking.save()

        sendemailSubject = 'Travel Booking Successfull' 

        sendemailContent = f"""
<html>
  
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     
   <title>Email From Travel</title>
</head>
  
<body>


<h1> <span style="color: #ffa500;">T</span>RAVEL</h1>
<b>Congratulations!</b><br>
<br>
<p>Dear, <b>{request.user}</b> </p><br>
Your Booking Are Successful for <b>{whereTo}</b> <br>
from <b>{arrivals}</b><br>
to <b>{leaving}</b><br>
<br>
<br>
<br>
<br><br><br>
<p>
    <b>Thank You!</b><br>
    Team <span style="color: #ffa500;">T</span>ravel
</p>


</body>
</html>

"""
        sendEmailtoUser(userEmail,sendemailSubject,sendemailContent)

        
        messages.success(request,'Booking Successful! 😊😊')
        return redirect('/')
    
    else:
        messages.error('Booking not successfully 😢😢')
        return redirect('/')

@login_required(login_url='/')
def myAllBooking(request):
    username = request.user
    mybook = BookSeat.objects.filter(username=username)
    mblist = []
    for myb in mybook.values_list():
        mblist.append(list(myb))
    
    content = {
        'con':mblist
    }

    return render(request,'mybooking.html',content)

def saveUserMessage(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            saveMsg = UserSavedMessages()
            saveMsg.name = name
            saveMsg.email = email
            saveMsg.number = number
            saveMsg.subject  = subject
            saveMsg.message  = message
            saveMsg.save()

            messages.success(request,'Your Message Save Successfull! 😊😊')
            return redirect('/')
    
        else:
            messages.error(request,'Sorry, Message Are Not Save 😢😢')
            return redirect('/')
    except:
        messages.error(request,'Sorry, Message Are Not Save 😢😢')
        return redirect('/')


