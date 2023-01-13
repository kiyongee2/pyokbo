from django.shortcuts import render, redirect
from common.forms import UserForm


# 회원 가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pybo:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


# 404 : 페이지를 찾을 수 없습니다.
def page_not_found(request, exception):
    return render(request, 'common/404.html', {})