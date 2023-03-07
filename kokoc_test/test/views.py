from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *


def pagination(request, qui):
    """
    Пагинация.
    """
    paginator = Paginator(qui, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


@login_required
def answer(request, id, id_q):
    """
    Отображение формы ответа, вопроса и вариантов ответа.
    """
    test = get_object_or_404(Test, pk=id)
    question = test.questions.get(id=id_q)
    answers = question.answers.all()
    last_question = test.questions.last()
    right_answer = question.num_of_right_answer

    form = QuestionForm
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            answer = int(form.cleaned_data['num_of_answer'])
            if answer == right_answer:
                user = request.user
                user.right_answers += 1
                user.save()

            if question.id == last_question.id:
                if user.right_answers == test.min_right_answers:
                    user.balance += test.reward
                    DoneTest.objects.create(user=request.user,
                                            test=test,
                                            done=True)
                else:
                    DoneTest.objects.create(user=request.user,
                                            test=test,
                                            done=False)
                user.right_answers = 0
                user.save()
                return redirect('test:index')
            return redirect('test:answer', id=id, id_q=id_q+1)

    context = {
        'question': question,
        'answers': answers,
        'form': form,
    }
    return render(request, 'test/answer.html', context)


@login_required
def start_test(request, id):
    """
    Запускает тест.
    """
    test = get_object_or_404(Test, pk=id)
    question = test.questions.first()
    return redirect('test:answer', id, question.id)


@login_required
def tests(request, id):
    """
    Для отображения всех вопросов.
    """
    test = get_object_or_404(Test, pk=id)
    questions = test.questions.all()
    count = len(questions)
    context = {
        'count': count,
        'page_obj': pagination(request, questions),
        'id': id,
    }
    return render(request, 'test/tests.html', context)


@login_required
def done_tests(request):
    """
    Страница выполненных тестов. И итога - пройден или нет.
    """
    tests = request.user.userdonetests.all()
    context = {
        'page_obj': pagination(request, tests),
    }
    return render(request, 'test/done_tests.html', context)


@login_required
def index(request):
    """
    Главная страница. Отображение всех непройденных Test.
    """
    donetests = DoneTest.objects.filter(user=request.user).values('test_id')
    tests = Test.objects.exclude(id__in=donetests)
    context = {
        'page_obj': pagination(request, tests),
    }
    return render(request, 'test/index.html', context)
