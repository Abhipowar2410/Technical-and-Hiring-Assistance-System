from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Student,certificate,exam,course,Manager,submit_test,Std_Result
from  django.contrib import messages
from django import forms

def front(request):
    return render(request,"index.html")


##################################################### STUDENT  OPRATIONS  ################################################################3
def sign_in(request):
    return render(request,"loginstudent.html")

def registration_student(request):
    return  render(request,"registration.html")
def student_signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        data= Student.objects.all().filter(email=email, password=password)
        if len(data) == 1:
            request.session["username"] = email  # session start
            messages.success(request, "Login Successfully")
            return redirect('/dashboard')
        else:
            messages.warning(request, "Incorrect Password And Username")
            return redirect('/')
    else:
        messages.warning(request, "Incorrect Password And Username")
        return redirect('sign_in')
def registration_save(request):
    if request.method == "POST":
        na = request.POST['name']
        em = request.POST['email']
        ph = request.POST['phone']
        pas = request.POST['password']
        ci = request.POST['city']
        co = request.POST['course']
        ge = request.POST['gender']
        py = request.POST['pyear']
        fi = request.FILES['file']

        s = Student(name=na, email=em, phone=ph, password=pas, city=ci, course=co, gender=ge, pyear=py, file=fi)
        s.save()  # insert the value
        messages.success(request, "Registration Successfully")
        return redirect('/')
    else:
        return HttpResponse("Fail")

def dashboard(request):
    if request.session.get('username') is not None:
        return render(request, "dashboard.html")
    else:
        return redirect('/')
def edit_profile(request):
    if request.session.get('username') is not None:
        email = request.GET["email"]
        data = Student.objects.all().filter(email=email)
        return render(request, "edit_profile.html", {'data': data})
    else:
        return redirect('/')
def update_data(request):
    if request.method == "POST":
        na = request.POST['name']
        em = request.POST['email']
        ph = request.POST['phone']
        pas = request.POST['password']
        ci = request.POST['city']
        co = request.POST['course']
        ge = request.POST['gender']
        py = request.POST['pyear']

        Student.objects.filter(email=em).update(name=na, email=em, phone=ph, password=pas, city=ci, course=co, gender=ge, pyear=py)
        messages.success(request, "Updated  Successfully")
        return redirect('/dashboard')
    else:
        return HttpResponse("Fail")

def add_certificate(request):
    if request.session.get('username') is not None:
        return render(request, "add_certificate.html")
    else:
        return redirect('/')
def certificate_save(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        ce_name=request.POST['certificate_name']
        date=request.POST['date']
        ce = request.FILES['certificate']
        c = certificate(name=name, email=email,certificate_name=ce_name ,date=date, file=ce)
        c.save()  # insert the value
        messages.success(request, "Certificate Added Successfully")
        return redirect('/dashboard')
    else:
        return HttpResponse("Fail")


def student_profile(request):
    if request.session.get('username') is not None:
        email = request.session.get('username')
        data = Student.objects.filter(email=email)
        data1 = certificate.objects.filter(email=email)

        if data.exists():
            student_email = data.first().email
            student_results = Std_Result.objects.filter(email=student_email)
        else:
            student_results = []

        return render(request, "student_profile.html", {
            'data': data,
            'data1': data1,
            'student_results': student_results
        })
    else:
        return redirect('/')


def add_cookie(request):
     res = HttpResponse("Cookie set")
     res.set_cookie("student_name","test")
     return res
def student_logout(request):
    del request.session["username"] #session end
    messages.warning(request, "logout Successfully")
    return redirect('/')


##################################################### COURSES ###########################################################
def course_list(request):
    return  render(request,"course.html")

class CourseSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, label='Search Course')
    course_type = forms.ChoiceField(choices=[

        ('Basic', 'Basic'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ], required=False, label='Course Type')

def search_courses(request):
    form = CourseSearchForm(request.GET)
    courses = course.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        course_type = form.cleaned_data.get('course_type')

        if query:
            courses = courses.filter(course__icontains=query)
        if course_type:
            courses = courses.filter(course_type=course_type)

    return render(request, 'search.html', {'form': form, 'courses': courses})


########################################################## HR OPRATIONS ################################################

def hr_login(request):
    return render(request,"hr_login.html")

def hr_registration(request):
    return render(request,"hr_login.html")

def hr_signupcheck(requset):
    if requset.method == "POST":
        em=requset.POST['email']
        ps=requset.POST['password']
        data = Manager.objects.all().filter(email=em,password=ps)
        if len(data) == 1:
            messages.success(requset, "Login Successfully")

            requset.session["username"]= em #session start

            return redirect("/HR_dashboard")
        else:
            messages.warning(requset, "Incorrect Password And Username")

            return redirect("/")

def HR_dashboard(request):
    if request.session.get('username') is not None:
        students = Student.objects.all()  # Get all students


        return render(request, "HR_dashboard.html", {'students': students})
    else:

        return redirect('/')

def hr_logout(request):
    del request.session["username"] #session end
    messages.warning(request, "logout Successfully")
    return redirect('/')



def hr_registration_save(request):
    if request.method == "POST":
        try:
            # Get form data
            na = request.POST['name']
            em = request.POST['email']
            ph = request.POST['contact_number']
            pas = request.POST['password']
            ci = request.POST['city']
            co = request.POST.get('company_name', '')
            ge = request.POST['gender']
            ed = request.POST.get('education', '')

            manager = Manager(
                name=na,
                email=em,
                password=pas,
                company_name=co,
                contact_number=ph,
                education=ed,
                city=ci,
                gender=ge
            )

            manager.save()

            messages.success(request, "HR Registration Successfully Completed")
            return redirect('/')

        except Exception as e:
            messages.error(request, f"Failed to register: {str(e)}")
            return redirect('/')

    else:
        return HttpResponse("Invalid Request")


def HR_edit_profile(request):
    if request.session.get('username') is not None:
        email = request.GET.get("email")
        data1 = Manager.objects.filter(email=email).first()
        if data1:
            return render(request, "HR_edit_profile.html", {'data1': data1})
        else:

            return redirect('/HR_dashboard')
    else:
        return redirect('/')


def HR_update_data(request):
    if request.session.get('username') is not None:
        if request.method == "POST":
            na = request.POST['name']
            em = request.POST['email']
            pas = request.POST['password']
            company = request.POST['company_name']
            ph = request.POST['contact_number']
            ed = request.POST['education']
            ci = request.POST['city']
            ge = request.POST['Gender']

            try:
                manager = Manager.objects.get(email=em)
                manager.name = na
                manager.password = pas
                manager.company_name = company
                manager.contact_number = ph
                manager.education = ed
                manager.city = ci
                manager.gender = ge
                manager.save()

                messages.success(request, "Profile updated successfully")
                return redirect('/HR_dashboard')
            except Manager.DoesNotExist:
                messages.error(request, "Manager not found")
                return redirect('/edit_profile')



    return render(request, '/')

def HR_profile(request):
    if request.session.get('username') is not None:
        email = request.session.get('username')
        data = Manager.objects.filter(email=email)
        return render(request, "HR_profile.html", {'data': data,})
    else:
        return redirect(request,'/')


def std_profile_for_hr(request, student_id):
    email = request.session.get('username')

    student = get_object_or_404(Student, id=student_id)

    cert = certificate.objects.filter(email=student.email)

    print(cert)
    student_results = Std_Result.objects.filter(email=student.email)

    context = {
        'students': [student],
        'cert': cert,
        'student_results': student_results
    }
    print(context)
    return render(request, 'student_profile_for_HR.html', context)

def search_students(request):
    query = request.GET.get('student_name', '')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.none()

    return render(request, 'student_search.html', {'students': students})



################################################## QUIZ /OPRATIONS  LOGIC ##################################################

def quiz(request, course_id, level):
    if request.session.get('username') is None:
        return redirect('/')

    course_obj = get_object_or_404(course, pk=course_id)

    questions = exam.objects.filter(course_type=course_obj, course_type__course_type=level)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        total_score = 0

        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')

            submit_test.objects.create(
                name=name,
                email=email,
                course=course_obj.course,
                course_type=level,
                question=question.question,
                answer=selected_option
            )

            if selected_option == question.correct_ans:
                total_score += 2

        Std_Result.objects.create(
            name=name,
            email=email,
            course=course_obj.course,
            course_type=level,
            marks=total_score
        )

        context = {
            'name': name,
            'email': email,
            'course': course_obj.course,
            'level': level,
            'total_score': total_score,
            'max_score': len(questions) * 2
        }

        # Render the result page
        return render(request, 'quiz_result..html', context)

    context = {
        'course': course_obj,
        'level': level,
        'questions': questions,
        'session_name': request.session.get('name', '')

    }

    return render(request, 'quiz.html', context)


def results(request):
    username = request.session.get('username')
    if username:
        results = Std_Result.objects.filter(user__username=username)
    else:
        results = Std_Result.objects.all()

    context = {
        'results': results
    }
    return render(request, 'quiz_result..html', context)

########################################################################################################################
def about(request):
    return render(request,"about.html")
