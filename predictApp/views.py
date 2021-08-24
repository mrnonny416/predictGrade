from django.shortcuts import redirect, render
from .loginforms import loginForm
from .models import Subject ,Subject_refer ,Instructor
# Create your views here.
def login(request):
    if request.method == 'POST':
        department = (request.POST.get('studentID'))[2:8]
        if department == '523206':
            request.session['studentID'] = request.POST.get('studentID')
            return redirect('select')
    return render(request, 'login.html', {'form': loginForm})

def select(request):
    studentID = request.session.get('studentID')
    if(studentID == None):
        return redirect('login')
    return render(request, 'select.html')

def forms(request):
    if request.method == 'GET':
        subject_refer_index = []
        subjectID = request.GET.get('subjectID')
        subject_info = Subject.objects.all()
        subject_refer_info = Subject_refer.objects.filter(subjectID=(subjectID))
        Instructor_info = Instructor.objects.all()
        for subject_info_roll in subject_info:
            for subject_refer_info_roll in subject_refer_info:
                if(subject_info_roll.subjectID == subject_refer_info_roll.ref_subjectID):
                    subject_refer_index.append(subject_info_roll.subjectID)
                    break
    return render(request, 'forms.html' ,{'subjectID':subjectID ,'subject_info':subject_info ,'subject_refer_info':subject_refer_info ,'Instructor_info':Instructor_info,'subject_refer_index':subject_refer_index})

def reports(request):
    if request.method == 'POST':
        InstructorID = []
        Grade = []
        subject_refer_index = []
        subjectID = request.GET.get('subjectID')
        subject_info = Subject.objects.all()
        subject_refer_info = Subject_refer.objects.filter(subjectID=(subjectID))
        Instructor_info = Instructor.objects.all()
        for subject_info_roll in subject_info:
            for subject_refer_info_roll in subject_refer_info:
                if(subject_info_roll.subjectID == subject_refer_info_roll.ref_subjectID):
                    subject_refer_index.append(subject_info_roll.subjectID)
                    break
        for subject_refer_index_roll in subject_refer_index:
            grade_roll = request.POST.get('grade_'+subject_refer_index_roll)
            if grade_roll == '4':Grade = 'A'
            elif grade_roll == '3.5':Grade = 'B+'
            elif grade_roll == '3':Grade = 'B'
            elif grade_roll == '2.5':Grade = 'C+'
            elif grade_roll == '2':Grade = 'C'
            elif grade_roll == '1.5':Grade = 'D+'
            elif grade_roll == '1':Grade = 'D'
            elif grade_roll == '0':Grade = 'F'
            else:Grade = 'ยังไม่ได้ลงทะเบียนเรียนหรือถอนรายวิชา'
            InstructorID.append([subject_refer_index_roll,request.POST.get('instructorID_'+subject_refer_index_roll),Grade])

    return render(request, 'reports.html', {'subjectID':subjectID ,'subject_info':subject_info ,'Instructor_info':Instructor_info,'subject_refer_index':subject_refer_index,'InstructorID':InstructorID})