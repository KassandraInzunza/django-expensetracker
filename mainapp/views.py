from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader

from django.views.generic import ListView
from django.views.generic.edit import CreateView

from django.urls import reverse

from mainapp.models import TransactionModel

# Create your views here.

def index(request):
    template = loader.get_template('main_index.html')
    context = {

    }

    return HttpResponse(template.render(context, request))

class SummaryListView(ListView):
    model = TransactionModel
    paginate_by = 5
    template_name = 'summary_list.html'

    def get_queryset(self, **kwargs):
        # memberId = self.kwargs['memberId']
        queryset = TransactionModel.objects.filter(member_id=1234).order_by('-created').all()
        return queryset

    def get_context_data(self, **kwargs):
        # memberId = self.kwargs['memberId']
        context = super(SummaryListView, self).get_context_data(**kwargs)
        return context

class ExpenseCreate(CreateView):
    model = TransactionModel
    fields = ['member_id', 'category', 'description', 'amount', ]
    template_name = 'expense_create.html'

    def get(self, *arg, **kwargs):
        return super(ExpenseCreate, self).get(*arg, **kwargs)

    def form_valid(self, form):
        self.object =  form.save(commit=False)
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(ExpenseCreate, self).get_context_data(**kwargs)
        return context

    '''
    def expense_create(request:HttpRequest):
        exp_create = TransactionModel(content = request.POST['amount'])
        exp_create.save()
        return redirect('/main/expense/')
    '''

    def get_success_url(self):
        return reverse('main-index')
