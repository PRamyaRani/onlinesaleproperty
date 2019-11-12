from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import CreatePlotModel,CreateAppartmentModel,CreateEmployeeModel
# Create your views here.
def index(request):
    return render(request,'index.html')

def user_login(request):
    un=request.POST['un']
    pw=request.POST['pw']
    print(un,pw)
    user=authenticate(request,username=un,password=pw)
    if user:
        login(request,user)
        return render(request,'welcome2.html')
    else:
        return render(request,'index.html',{'msg':"Invalid_Details"})

def addplot(request):

    return render(request,"addplot.html")


def editplot(request):
    return render(request,"editplot.html")


def viewplot(request):
    return render(request,"viewplot.html")


def addappartment(request):
    return render(request,"addappartment.html")


def editappartment(request):
    return render(request,"editappartment.html")


def viewappartment(request):
    return render(request, "viewappartment.html")


def addemployee(request):
    return render(request, "addemployee.html")


def editemployee(request):
    return render(request, "editemployee.html")


def deleteemployee(request):

    return render(request, "delete_employee.html")

def homepage(request):
    return render(request,"homepage.html")

def saveplot(request):
    Plot_no = request.POST.get("pn")
    Road_no = request.POST.get("rn")
    Survey_no = request.POST.get("sn")
    Cost_per_Sqd = request.POST.get("cps")
    total_sqd = request.POST.get("ts")
    Otherexpances = request.POST.get("oe")
    Boundaries = request.POST.get("bd")
    Facing = request.POST.get("fc")
    Status = request.POST.get("st")
    Totalcost = request.POST.get("tc")
    CreatePlotModel(PLOT_NO=Plot_no,ROAD_NO=Road_no,SURVEY_NO=Survey_no,COST_PER_SQD=Cost_per_Sqd,TOTAL_SQD=total_sqd,Other_EXPENCES=Otherexpances,BOUNDARIES=Boundaries,FACING=Facing,STATUS=Status,TOTAL_COAST=Totalcost).save()
    return render(request,"homepage.html")


def view_plot_details(request):
    Plot_no = request.POST.get("plot_no")
    object = CreatePlotModel.objects.get(PLOT_NO=Plot_no)
    return render(request,"view_plot_details.html",{"plot_data":object})


def editplot_details(request):
    Plot_no = request.POST.get("plot_no")
    object_edit = CreatePlotModel.objects.get(PLOT_NO=Plot_no)
    return render(request, "view_plot_details.html", {"plot_data_edit": object_edit})


def update_plot(request):
    Plot_no = request.POST.get("plot_no")
    Road_no = request.POST.get("road_no")
    Survey_no = request.POST.get("survey_no")
    Cost_per_Sqd = request.POST.get("cost_sqd")
    Total_sqd = request.POST.get("total_sqd")
    Otherexpances = request.POST.get("other_expence")
    Boundaries = request.POST.get("boundaries")
    Facing = request.POST.get("facing")
    Status = request.POST.get("status")
    Totalcoast = request.POST.get("total_coast")
    print(Totalcoast)

    res=CreatePlotModel.objects.get(PLOT_NO=Plot_no)
    res.ROAD_NO=Road_no
    res.SURVEY_NO=Survey_no
    res.COST_PER_SQD=Cost_per_Sqd
    res.TOTAL_SQD=Total_sqd
    res.Other_EXPENCES=Otherexpances
    res.BOUNDARIES=Boundaries
    res.FACING=Facing
    res.STATUS=Status
    res.TOTAL_COAST=Totalcoast
    res.save()
    return render(request,"homepage.html")


def saveappartment(request):
    Appartment_no = request.POST.get("an")
    Road_no = request.POST.get("rn")
    Survey_no = request.POST.get("sn")
    Cost_per_Sqd = request.POST.get("cps")
    total_sqd = request.POST.get("ts")
    Otherexpances = request.POST.get("oe")
    Boundaries = request.POST.get("bd")
    Facing = request.POST.get("fc")
    Status = request.POST.get("st")
    Totalcost = request.POST.get("tc")
    CreateAppartmentModel(APPARTMENT_NO=Appartment_no,ROAD_NO=Road_no,SURVEY_NO=Survey_no,COST_PER_SQD=Cost_per_Sqd,TOTAL_SQD=total_sqd,Other_EXPENCES=Otherexpances,
                    BOUNDARIES=Boundaries,FACING=Facing,STATUS=Status,TOTAL_COAST=Totalcost).save()
    return render(request,"homepage.html")
def view_appart_details(request):
    Appartment_no = request.POST.get("APPARTMENT_NO")
    print(Appartment_no)
    object = CreateAppartmentModel.objects.get(APPARTMENT_NO=Appartment_no)
    print(object)
    return render(request,"view_appart_details.html",{"appart_data":object})

#def view_plot_details(request):
 #  object = CreatePlotModel.objects.get(PLOT_NO=Plot_no)
  #  return render(request,"view_plot_details.html",{"plot_data":object})

def edit_appart_details(request):
    Appartment_no  = request.POST.get("APPARTMENT_NO")
    object_edit = CreateAppartmentModel.objects.get(APPARTMENT_NO=Appartment_no)
    return render(request, "view_appart_details.html", {"appart_data_edit": object_edit})

def update_appart(request):
        Appartment_no = request.POST.get("appart_no")
        Road_no = request.POST.get("road_no")
        Survey_no = request.POST.get("survey_no")
        Cost_per_Sqd = request.POST.get("cost_sqd")
        Total_sqd = request.POST.get("total_sqd")
        Otherexpances = request.POST.get("other_expence")
        Boundaries = request.POST.get("boundaries")
        Facing = request.POST.get("facing")
        Status = request.POST.get("status")
        Totalcoast = request.POST.get("total_coast")
        print(Totalcoast)

        res = CreateAppartmentModel.objects.get(APPARTMENT_NO=Appartment_no)
        res.ROAD_NO = Road_no
        res.SURVEY_NO = Survey_no
        res.COST_PER_SQD = Cost_per_Sqd
        res.TOTAL_SQD = Total_sqd
        res.Other_EXPENCES = Otherexpances
        res.BOUNDARIES = Boundaries
        res.FACING = Facing
        res.STATUS = Status
        res.TOTAL_COAST = Totalcoast
        res.save()
        return render(request, "homepage.html")


def saveemployee(request):
    Employee_name = request.POST.get("en")
    Employee_id = request.POST.get("eid")
    Employee_email = request.POST.get("eemail")
    Employee_location = request.POST.get("el")
    Employee_doj = request.POST.get("edoj")
    Employee_role = request.POST.get("erole")
    Employee_qual = request.POST.get("equal")
    Employee_remarks = request.POST.get("er")
    CreateEmployeeModel(EMPLOYEE_NAME=Employee_name,EMPLOYEE_ID=Employee_id,EMPLOYEE_EMAIL=Employee_email,EMPLOYEE_LOCATION=Employee_location,EMPLOYEE_DOJ=Employee_doj,EMPLOYEE_ROLE=Employee_role,EMPLOYEE_QUAL=Employee_qual,EMPLOYEE_REMARKS=Employee_remarks).save()
    return render(request,"homepage.html")


def view_employee_details(request):
    employee_id = request.POST.get("Employee_Id")
    object = CreatePlotModel.objects.get(EMPLOYEE_ID=employee_id)
    return render(request,"view_employee_details.html",{"employee_data":object})

def editemployee_details(request):
    employee_id = request.POST.get("eid")

    object_edit = CreateEmployeeModel.objects.get(EMPLOYEE_ID=employee_id)
    return render(request, "view_employee_details.html", {"employee_data_edit": object_edit})

def update_employee(request):
    Employee_name = request.POST.get("employee_name")
    Employee_id = request.POST.get("employee_id")
    Employee_email = request.POST.get("employee_email")
    Employee_location = request.POST.get("employee_location")
    Employee_doj = request.POST.get("employee_doj")
    Employee_role = request.POST.get("employee_role")
    Employee_qual = request.POST.get("employee_qual")
    Employee_remarks = request.POST.get("employee_remarks")

    res=CreateEmployeeModel.objects.get(EMPLOYEE_NAME=Employee_name)
    res.EMPLOYEE_ID=Employee_id
    res.EMPLOYEE_EMAIL=Employee_email
    res.EMPLOYEE_LOCATION=Employee_location
    res.EMPLOYEE_DOJ=Employee_doj
    res.EMPLOYEE_ROLE=Employee_role
    res.EMPLOYEE_QUAL=Employee_qual
    res.EMPLOYEE_REMARKS=Employee_remarks
    res.save()
    return render(request, "homepage.html")


def delete_employee_details(request):
    employee_id = request.POST.get("eid")
    CreateEmployeeModel.objects.get(EMPLOYEE_ID=employee_id).delete()
    return render(request, "homepage.html")