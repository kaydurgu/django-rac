from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Contest, Question, Result

class AllContestView(ListView):

    template_name = 'contest/all_contest.html'
    model = Contest
    def get(self, request , *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ContestDetailView(DetailView):
    template_name = 'contest/contest_detail.html'
    model = Contest
    context_object_name = 'contest'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contest = get_object_or_404(Contest, pk = context['object'].pk)
        self.contest = contest
        context['questions'] = contest.questions.all()
        return context
    def get(self, request, *args, **kwargs):
        contest = get_object_or_404(Contest, pk = kwargs['pk'])
        if Result.objects.filter(contest = contest, participant = request.user.profile).exists() and not request.user.is_staff:
            messages.warning(request,'You have already token this exam')
            return redirect('all-contest')
        return super().get(request, *args, **kwargs)

class ContestResultView(TemplateView):
    template_name = 'contest/contest_result.html'
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['results'] = Result.objects.filter(contest_id = kwargs['pk']).order_by('-score')
        return context

    def post(self, request, *args, **kwargs):
        true_answers = list(request.POST.values()).count('True')
        contest = get_object_or_404(Contest, pk = kwargs['pk'])
        k = Result.objects.filter(contest = contest, participant = request.user.profile).exists()
        if not k:
            res = Result(participant = request.user.profile , contest = contest , score = true_answers)
            res.save()
        else:
            messages.warning(request, 'You already token this contest')
            return redirect('all-contest')
        return render(request, 'contest/contest_result.html',{'results':  Result.objects.filter(contest_id = kwargs['pk']).order_by('-score') })
    
