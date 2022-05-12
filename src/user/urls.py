from django.urls import path
from . import list_views
from . import cnpj_views
from . import cpf_views

urlpatterns = [
    path('listAll/common', list_views.all_common, name="all_common"),
    path('listAll/cpf', cpf_views.all_cpf, name="all_cpf"),
    path('listAll/cnpj', cnpj_views.all_cnpj, name="all_cnpj"),
    path('listAll/segment', list_views.all_segment, name="all_segment"),
    path('listAll/gender', list_views.all_gender, name="all_gender"),
    path('listAll/civil', list_views.all_civil, name="all_civil"),
    path('listOne/cnpj/<int:user_cnpj_id>', cnpj_views.one_cnpj, name='one_cnpj'),
    path('listOne/cpf/<int:user_cpf_id>', cpf_views.one_cpf, name='one_cpf'),
    path('listCity/perState/<str:state>', list_views.city_per_state, name='city_per_state'),

    path('create/cnpj', cnpj_views.create_cnpj, name="create_cnpj"),
    path('create/cpf', cpf_views.create_cpf, name="create_cpf")
]