from django.shortcuts import render

# Create your views here.

def index_view(request):
    context = {
        'name': 'Mohammad Hossein Sangestani',
        'skill': 'Django Developer',
        'about_me': 'I am a mechatronics engineering student, I am interested in website development using Django framework'
    }
    return render(request, 'website/index.html',context)


def contact_view(request):
    return render(request, 'website/contact.html')


def portfolio_view(request):
    context = {
        'project_name': 'tour guide website'
    }
    return render(request, 'website\portfolio.html', context)


def resume_view(request):
    context = {
        'field_of_study': 'Mechatronics',
        'date': '2022 - 2024',
        'experience': 'I had the opportunity to study computer mechanics and electricity'
    }
    return render(request, 'website/resume.html', context)