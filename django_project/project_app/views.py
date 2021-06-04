from django.shortcuts import render
# from project_app.models import User
from project_app.forms import NewUserForm

def index(request):
    return render(request, 'project_app/index.html')

def users(request):
    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users':user_list}
    # return render(request, 'project_app/users.html', context=user_dict)

    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: Form Invalid!')

    return render(request, 'project_app/users.html', {'form':form})
