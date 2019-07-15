from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Topics
from django.views import generic
# Create your views here.

class ListView(generic.ListView):
	template_name = 'topics/index.html'
	context_object_name = 'latest_topics'

	def get_queryset(self):
		return Topics.objects.order_by('-topic_date')[:10]

class DetailView(generic.DetailView):
	model = Topics
	template_name = 'topics/topics_detail.html'


def list(request):
	latest_topics = Topics.objects.all()[:10]
	context = {
		'latest_topics': latest_topics,
	}
	return render(request, 'topics/index.html', context)

def detail(request, topic_id):
	topic = get_object_or_404(Topics, pk=topic_id)
	
	return render(request, 'topics/topics_detail.html', {'topic': topic})
