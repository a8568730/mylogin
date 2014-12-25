from django.shortcuts import render
from sui2.models import 使用者表格

def 新增一個使用者(request):
    if request.method == 'POST':
        新使用者 = 使用者表格(request.POST)
        if 新使用者.is_valid():
            儲存 = 新使用者.save()
    else:
        新使用者 = 使用者表格()
    return render(request, 'add_user.html', {
        '新使用者': 新使用者,
    })