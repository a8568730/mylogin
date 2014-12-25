from django.shortcuts import render

def 新增一個使用者(request):
    if request.method == 'POST':
        新使用者 = 使用者表格(request.POST)
        新使用者.save()
    
    return render(request, 'sui2/add_user.html', {
        '新使用者': 新使用者,
    })