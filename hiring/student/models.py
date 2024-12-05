from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    pyear = models.IntegerField()
    file = models.FileField(upload_to='resumes', blank=True, null=True)

    def __str__(self):
        return self.name

class certificate(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the 'id' field (auto-incremented)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    certificate_name=models.CharField(max_length=50)
    date=models.DateField()
    file = models.FileField(upload_to='certificate', blank=True, null=True)

    def __str__(self):
        return self.name


class course(models.Model):
    course=models.CharField(max_length=200)
    course_type =models.CharField(max_length=200)

    def __str__(self):
        return self.course

class exam(models.Model):
    course_type = models.ForeignKey(course, on_delete=models.CASCADE)
    question=models.CharField(max_length=200)
    optionA=models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD= models.CharField(max_length=100)
    correct_ans=models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(exam, on_delete=models.CASCADE)
    marks = models.IntegerField()
    total_questions = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student

########################### HR  MODELS ######################################

class Manager(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    contact_number=models.IntegerField(default="0")
    education=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)


    def __str__(self):
        return self.name


#########################################   TEST/RESULTS MODELS #######################################################################


class submit_test(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    course = models.CharField(max_length=200)
    course_type = models.CharField(max_length=200)
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=50)

    def __str__(self):
        return self.question

class Std_Result(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    course = models.CharField(max_length=200)
    course_type = models.CharField(max_length=200)
    marks = models.IntegerField()

    def __str__(self):
        return self.name