from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.db.models import Q
from .models import Average, Query
from .forms import QueryForm
from .filters import QueryFilter
from django.db.models import Avg, Max, Min, FloatField
from django.template.loader import render_to_string
import matplotlib.pyplot as plt
import io
import urllib, base64
from plotly.offline import plot
from plotly.graph_objs import Scatter

class QueryMakeModel(FormView):
		template_name = 'QueryMakeModel.html'
		success_url = '/data/'
		form_class = QueryForm
		
		def form_valid(self, form):
			return HttpResponse("Sweet.")
		
def index(request):

	if request.method == 'POST':
		FormSite = QueryForm(request.POST)
		if FormSite.is_valid():
			pass
	else:
		FormSite = QueryForm()

	return render(request, 'app/QueryMakeModel.html', {'FormSite': FormSite})
		
def data(request):
	if request.method == 'GET':

		FormMake = request.GET.get('MAKE')
		FormModel = request.GET.get('MODEL')
		FormFuel = request.GET.get('FUEL')
		FormLiter = request.GET.get('LITER')
		FormYear = request.GET.get('YEAR')
		
		lookups= Q(fuel__icontains=FormFuel) & Q(liter__icontains=FormLiter) & Q(year__icontains=FormYear) & Q(make__icontains=FormMake) & Q(model__icontains=FormModel)

		query_results= Average.objects.filter(lookups).distinct()
		
		avg_price = query_results.aggregate(Avg('price'))
		
		totalno_prices = query_results.count()
		
		max_price = query_results.aggregate(Max('price'))
		
		min_price = query_results.aggregate(Min('price'))
		
		difference_price = query_results.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))
		
		#past_avg = render_to_string('db.html', { 'avg_price': avg_price })
		
		x_data = [min_price, max_price]
		y_data = [avg_price]
		plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='markers', name='Visualization',
                        opacity=0.8, marker_color='green')],
               output_type='div')
		
		"""
		plt.plot(range(10))
		fig = plt.gcf()
		buf = io.BytesIO()
		fig.savefig(buf, format='png')
		buf.seek(0)
		string = base64.b64encode(buf.read())
		uri = urllib.parse.quote(string)
		"""
		
		context = { 
			'avg_price': avg_price,
			'totalno_prices': totalno_prices,
			'max_price': max_price,
			'min_price': min_price,
			'difference_price': difference_price,
			'query_results': query_results,
			'plot_div': plot_div,
			#'data': uri,
			#'past_avg': past_avg,
		}
				
		return render(request, 'app/db.html', context)

