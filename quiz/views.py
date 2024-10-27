from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Result, Question
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest


# View for listing all quizzes
@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

# View for quiz detail
@login_required
def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})


@login_required
def quiz_take(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.get_questions()
    
    # Simpan ID pertanyaan dalam sesi
    request.session['quiz_questions'] = [q.id for q in questions]
    
    return render(request, 'quiz/quiz_take.html', {'quiz': quiz, 'questions': questions})


# @login_required
# def quiz_submit(request, pk):
#     if request.method == "POST":
#         quiz = get_object_or_404(Quiz, pk=pk)
#         question_ids = request.session.get('quiz_questions', [])
#         questions = Question.objects.filter(id__in=question_ids).order_by('id')
        
#         score = 0
#         correct_answers = 0
#         question_details = []

#         for question in questions:
#             selected_answer = request.POST.get(f'question_{question.id}')
#             is_correct = selected_answer == question.correct_answer
            
#             if is_correct:
#                 correct_answers += 1
            
#             question_details.append({
#                 'title': question.title,
#                 'selected_answer': selected_answer,
#                 'correct_answer': question.correct_answer,
#                 'is_correct': is_correct
#             })

#         total_questions = len(questions)
#         score = (correct_answers / total_questions) * 100

#         Result.objects.create(quiz=quiz, user=request.user, score=score)
        
#         passed = score >= quiz.required_score_to_pass

#         # Hapus data sesi setelah digunakan
#         if 'quiz_questions' in request.session:
#             del request.session['quiz_questions']

#         return render(request, 'quiz/quiz_result.html', {
#             'quiz': quiz,
#             'score': score,
#             'passed': passed,
#             'total_questions': total_questions,
#             'correct_answers': correct_answers,
#             'question_details': question_details
#         })
#     return redirect('quiz_list')

@login_required
def scores_quiz(request):  
  user_id = request.user.id  
  results = Result.objects.filter(user_id=user_id).order_by('-created')   
  return render(request, 'quiz/results.html', {'results': results})


@login_required
def quiz_submit(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    
    if request.method == "POST":
        question_ids = request.session.get('quiz_questions', [])
        if not question_ids:
            return HttpResponseBadRequest("Quiz session expired. Please start the quiz again.")

        questions = Question.objects.filter(id__in=question_ids).order_by('id')
        
        score = 0
        correct_answers = 0
        question_details = []

        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            is_correct = selected_answer == question.correct_answer
            
            if is_correct:
                correct_answers += 1
            
            question_details.append({
                'title': question.title,
                'selected_answer': selected_answer,
                'correct_answer': question.correct_answer,
                'is_correct': is_correct
            })

        total_questions = len(questions)
        score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

        result = Result.objects.create(quiz=quiz, user=request.user, score=score)
        
        passed = score >= quiz.required_score_to_pass

        # Simpan hasil di sesi
        request.session['quiz_result'] = {
            'result_id': result.id,
            'score': score,
            'passed': passed,
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'question_details': question_details
        }

        # Hapus data sesi quiz_questions setelah digunakan
        if 'quiz_questions' in request.session:
            del request.session['quiz_questions']

        return redirect('quiz_result', pk=pk)
    
    elif request.method == "GET":
        # Jika ini adalah permintaan GET, coba ambil hasil dari sesi
        quiz_result = request.session.get('quiz_result')
        if quiz_result and Result.objects.filter(id=quiz_result['result_id'], quiz=quiz, user=request.user).exists():
            return render(request, 'quiz/quiz_result.html', {
                'quiz': quiz,
                **quiz_result
            })
        else:
            # Jika tidak ada hasil dalam sesi, redirect ke daftar kuis
            return redirect('quiz_list')

    return redirect('quiz_list')

@login_required
def quiz_result(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    quiz_result = request.session.get('quiz_result')
    
    if quiz_result and Result.objects.filter(id=quiz_result['result_id'], quiz=quiz, user=request.user).exists():
        # Hapus hasil dari sesi setelah ditampilkan
        del request.session['quiz_result']
        return render(request, 'quiz/quiz_result.html', {
            'quiz': quiz,
            **quiz_result
        })
    else:
        # Jika tidak ada hasil dalam sesi, ambil hasil terakhir dari database
        result = Result.objects.filter(quiz=quiz, user=request.user).order_by('-created').first()
        if result:
            return render(request, 'quiz/quiz_result.html', {
                'quiz': quiz,
                'score': result.score,
                'passed': result.score >= quiz.required_score_to_pass,
                # Anda mungkin perlu menambahkan lebih banyak data di sini
            })
        
def result_quiz_all(request):
    all_results = Result.objects.all().order_by('-id')
    return render(request, 'quiz/all_quiz_results.html', {'all_results': all_results})