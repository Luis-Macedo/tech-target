from django.urls import path

from . import question_views
from . import answer_views
from . import form_views

urlpatterns = [
    path('listAnswers/perUser/<int:user_cpf_id>', answer_views.list_answer_per_user, name="list_answer_per_user"),
    path('listAnswers/perQuestion/<int:form_id>/<int:question_id>', answer_views.list_answer_per_question, name="list_answer_per_question"),
    path('listAnswers/perForm/<int:form_id>', answer_views.list_answer_per_form, name="list_answer_per_form"),
    path('listForms/perUser/<int:user_cnpj_id>', form_views.list_form_per_user, name="list_form_per_user"),
    path('listForms/perSegment/<int:segment_id>', form_views.list_form_per_segment, name="list_form_per_segment"),
    path('listQuestions/perForm/<int:form_id>', question_views.list_per_form, name="list_per_form"),
]