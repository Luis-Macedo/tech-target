from django.urls import path

from .questions import question_views
from .answers import answer_views
from .form import form_views

urlpatterns = [
    path('listAnswers/perUser/<int:user_cpf_id>', answer_views.list_answer_per_user, name="list_answer_per_user"),
    path('listAnswers/perQuestion/<int:question_id>', answer_views.list_answer_per_question, name="list_answer_per_question"),
    path('listAnswers/perForm/<int:form_id>', answer_views.list_answer_per_form, name="list_answer_per_form"),
    path('listForms/perUser/<int:user_cnpj_id>', form_views.list_form_per_user, name="list_form_per_user"),
    path('listForms/perSegment/<int:segment_id>', form_views.list_form_per_segment, name="list_form_per_segment"),
    path('listForms/allForms', form_views.list_all_forms, name="listAll"),
    path('listQuestions/perForm/<int:form_id>', question_views.list_per_form, name="list_per_form"),
    path('listQuestions/types', question_views.list_types, name="listTypes"),

    path('create/<int:user_cnpj_id>', form_views.create_form, name="createForm"),
    path('insert/answers/<int:user_cpf_id>', answer_views.insert_answers, name="insertAnswers")
]