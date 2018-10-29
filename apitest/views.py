from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from apitest.models import Apistep,Apitest,Apis
from django.contrib.auth.decorators import login_required
# Create your views here.
def test(request):
    return HttpResponse("Hello World")

#平台登录Login
def login(request):
    if request.POST:
        username = password = ''
        #获取前端输入的username
        username = request.POST.get('username')
        password = request.POST.get('password')
        #auth模块时django自带的用户认证模块authenticate()会在该 User 对象上设置一个属性来标识后端已经认证了该用户，且该信息在后续的登录过程中是需要
        user = auth.authenticate(username=username, password=password)
        #当拿到的用户对象存在是说明认证成功，返回的是一个用户对象，认证是吧则返回一个none
        if user is not None and  user.is_active:
            #将登陆成功的返回的user对象传入，这样就可以记录下用户的登录状态，(在全局存储用户信息，在任何视图函数都可以取出来)，人家有什么参数就传什么
            auth.login(request,user)
            #session对象的作用域为一次会话，通常浏览器不关闭，保存的值就不会消失，当然也会出现session超时
            request.session['user'] = username
            #成功后跳转home页面
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error':'username or passowrd roor'})
    return render(request,'login.html')

#登录后跳转页面
def home(request):
    return render(request,'home.html')

#退出功能实现
def logout(request):
    auth.logout(request)
    return render(request,'login.html')

#接口管理
#调用前需要用户登录
@login_required
def apitest_manage(request):
    #读取所有流程接口数据
    apitest_list = Apitest.objects.all()
    #读取浏览器登录的session
    username = request.session.get('user','')
    #定义流程接口数据的变量并返回到前端
    return render(request,'apitest_manage.html',{'user':username,'apitests':apitest_list})

#接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user','')
    apistep_list = Apistep.objects.all()
    return render(request,'apistep_manage.html',{'user':username,'apisteps':apistep_list})

#单接口管理
@login_required
def apis_manage(request):
    username = request.session.get('user','')
    apis_list = Apis.objects.all()
    return render(request,'apis_manage.html',{"username":username,'apiss':apis_list})