from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from set.models import Set
#加入Django自带模型auth.models 可以直接引用User
from django.contrib.auth.models import User

# Create your views here.


@login_required
def set_manage(request):
    username = request.session.get('user','')
    set_list = Set.objects.all()
    return render(request,'set_manage.html',{'username':username,'sets':set_list})

#用户管理
@login_required
def set_user(request):
    username = request.session.get('user','')
    user_list = User.objects.all()
    return render(request,'set_user.html',{'username':username,'users':user_list})