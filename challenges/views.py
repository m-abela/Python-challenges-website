from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Challenge, Student

@login_required(login_url='login')
def challenge_view(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/challenge_list.html', {'challenges': challenges})


def leaderboard_view(request):
    students = Student.objects.order_by('-points')
    return render(request, 'challenges/leaderboard.html', {'students': students})


def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    return render(request, 'challenges/challenge_detail.html', {'challenge': challenge})


@login_required
def submit_solution(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    if request.method == 'POST':
        user = request.user  # Get the current logged-in login

        # Find or create the associated Student record
        student, created = Student.objects.get_or_create(user=user)

        submitted_answer = request.POST.get('solution')  # Get the submitted answer
        #print(challenge.answer, submitted_answer)
        is_correct = (submitted_answer == challenge.answer)

        if is_correct:
            student.points += 10  # Replace 10 with the actual number of points for this challenge
            student.save()
            return redirect('challenge_success')  # Redirect to a success page
        else:
            return redirect('challenge_fail')

    return render(request, 'submit_solution.html', {'challenge': challenge})

def challenge_success(request):
    return render(request, 'challenges/challenge_success.html')

def challenge_fail(request):
    return render(request, 'challenges/challenge_fail.html')

def writing(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/index.html', {'challenges': challenges})