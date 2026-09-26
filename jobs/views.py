from django.shortcuts import render, get_object_or_404, redirect
from.models import Job, Category, Application
from django.contrib import messages

# Create your views here.


def job_list(request):
    jobs = Job.objects.filter(is_active=True).select_related('category', 'employer')
    categories = Category.objects.all()
    
    query = request.GET.get('q')
    category_slug = request.GET.get('category')
    job_type = request.GET.get('type')
    
    if query:
        jobs = jobs.filter(title__icontains=query)
    if category_slug:
        jobs = jobs.filter(category__slug=category_slug)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
        
    context = {
        'jobs': jobs.order_by('-created_at'),
        'categories': categories,
    }
    return render(request, 'jobs/job_list.html', context)


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    
    # Check if logged-in user already applied
    has_applied = False
    if request.user.is_authenticated:
        has_applied = Application.objects.filter(job=job, applicant=request.user).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        if has_applied:
            messages.warning(request, "You have already applied for this position.")
            return redirect('job_detail', pk=job.pk)
        
        resume = request.FILES.get('resume')
        cover_letter = request.POST.get('cover_letter', '')
        
        if resume:
            Application.objects.create(
                job=job,
                applicant=request.user,
                resume=resume,
                cover_letter=cover_letter
            )
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('job_detail', pk=job.pk)

    return render(request, 'jobs/job_detail.html', {'job': job, 'has_applied': has_applied})