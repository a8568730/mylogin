from django.shortcuts import render
from sui2.表格 import 加使用者表格
from django.http.response import HttpResponse
from sui2.models import 使用者表格
import json



def 新增一個使用者(request):
	if request.method == 'POST':
		新使用者 = 加使用者表格(request.POST)
		if 新使用者.is_valid():
			新使用者.save()
	else:
		新使用者 = 加使用者表格()
	return render(request, 'add_user.html', {
		'新使用者': 新使用者,
	})
	
	
def 顯示所有使用者(request):
	全部使用者 = []
	for 使用者 in 使用者表格.objects.all():
		全部使用者.append([使用者.username, 使用者.password])
	return HttpResponse(json.dumps(全部使用者, ensure_ascii=False), content_type="application/json; charset=utf-8")   

	