from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice

from django.template import loader

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse


from django.views import generic

# Option 3: Inherit from generic view
class IndexView(generic.ListView):

    template_name = "polls/index.html"
    context_object_name = "lastest_questions"

    def get_queryset(self):
        return Question.objects.order_by("-publish_date")[:5]

class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    model = Question

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"





# def index(request):
#     # return lastest question by publish dates (top 5)
#     lastest_questions = Question.objects.order_by("-publish_date")[:5]
#
#     # Option 1: Load template by loader
#     # template = loader.get_template("polls/index.html")
#     # context = {
#     #     "lastest_questions": lastest_questions
#     # }
#     # return HttpResponse(template.render(context, request))
#
#     # Option 2: use shortcut render
#     context = {
#         "lastest_questions": lastest_questions
#     }
#     return render(request, "polls/index.html", context)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#
#     return render(request, "polls/detail.html", {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))
#
# def results(request, question_id):
#
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
#     # return HttpResponse(f"You're getting result at question: {question_id}")
