from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from . models import Tes, QuestionSains, ResultSains

def sains_list(request):
  tes_all = Tes.objects.all()
  return render(request, 'sains/list.html', {'tes_all': tes_all})


@login_required
def sains_detail(request, pk):
    tes = get_object_or_404(Tes, pk=pk)
    return render(request, 'sains/detail.html', {'tes': tes})

@login_required
def sains_take(request, pk):
    tes = get_object_or_404(Tes, pk=pk)
    questions = tes.get_questions()
    print(questions)
    return render(request, 'sains/take.html', {'tes': tes, 'questions': questions})

# Submit the tes and calculate score
@login_required
def sains_submit(request, pk):
    if request.method == "POST":
        # Get the quiz by primary key (pk)
        tes = get_object_or_404(Tes, pk=pk)
        
        # Retrieve the questions for the quiz
        questions = tes.get_questions()
        score = 0
        correct_answers = 0

        # List to store question details with user's answers
        question_details = []

        # Iterate through the questions to check the user's selected answers
        for question in questions:
            # Get the selected answer from the POST data
            selected_answer = request.POST.get(f'question_{question.id}')
            is_correct = selected_answer == question.correct_answer
            
            # Increment the correct_answers count if the selected answer matches the correct answer
            if is_correct:
                correct_answers += 1
            
            # Append the question details to the list
            question_details.append({
                'title': question.title,
                'selected_answer': selected_answer,
                'correct_answer': question.correct_answer,
                'is_correct': is_correct
            })

        # Calculate total number of questions
        total_questions = tes.number_of_questions
        
        # Calculate the score as a percentage
        score = (correct_answers / total_questions) * 100

        # Save the result to the Result model
        result = ResultSains.objects.create(tes=tes, user=request.user, score=score)
        
        # Determine if the user passed
        passed = score >= tes.required_score_to_pass

        return render(request, 'sains/sains_result.html', {
            'tes': tes,
            'score': score,
            'passed': passed,
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'question_details': question_details  # Pass question details to the template
        })
    return redirect('tes_sains_list')

@login_required
def scores_sains(request):  
  user_id = request.user.id  
  results = ResultSains.objects.filter(user_id=user_id).order_by('-score')   
  return render(request, 'sains/results.html', {'results': results})


def result_sains_all(request):
    all_results = ResultSains.objects.all().order_by('-id')
    return render(request, 'sains/all_sains_results.html', {'all_results': all_results})