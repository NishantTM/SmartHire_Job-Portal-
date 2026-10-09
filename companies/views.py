<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from .forms import CompanyForm
from .models import Company


@login_required
def company_create(request):
    # Only recruites can create a company
    if request.user.role != "RECRUITER":
        return redirect("home")
    
    # one recruiter can have only one company 
    if hasattr(request.user, "company"):
        return redirect("Company_dashboard")
    
    
    if request.mehod == "POST":
        form = CompanyForm(request.POST, request.FILES)
        
    if form.is_valid():
        company = form.save(commit=False)
        company.recruiter = request.user
        company.save()
        
        return redirect("company_dashboard")
    
    else:
        form = CompanyForm()

    return render(
        request,
        "companies/company_create.html",
        {"form": form},
    )
    
@login_required 
def company_dashboard(request):
    if request.user.role != "RECRUITER":
        return redirect("home")
    
    company = get_object_or_404(Company,recruiter=request.user, )
    
    return render(
        request,
        "companies/company_dashboard.html",
        {"company": company},
    )
    
@login_required 
def company_detail(request):
    
    company = get_object_or_404(Company, recruiter=request.User, )
    return render(request, "companies/company_detail/html",{"company": company},)
    
@login_required
def company_edit(request):
    if request.user.role != "RECRUITER":
        return redirect("home")

    company = get_object_or_404(
        Company,
        recruiter=request.user,
    )

    if request.method == "POST":
        form = CompanyForm(
            request.POST,
            request.FILES,
            instance=company,
        )

        if form.is_valid():
            form.save()
            return redirect("company_dashboard")

    else:
        form = CompanyForm(instance=company)

    return render(
        request,
        "companies/company_edit.html",
        {"form": form, "company": company},
    )
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 1bf5e7ac4d7554eaa72a7d6f65cb20b81b9d48b6
