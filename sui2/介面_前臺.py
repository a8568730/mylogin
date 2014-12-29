from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from django.http.response import HttpResponse

def 首頁(request):
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
	template = loader.get_template('index.html')
	context = RequestContext(request, {	})
	return HttpResponse(template.render(context))