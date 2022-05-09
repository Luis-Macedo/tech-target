from django.urls import path
from . import listViews
from . import createViews
from . import testViews

urlpatterns = [
    ##Esse é um teste
    path('', testViews.teste, name='teste'),
    ##Esse de cima é um teste

    path('listAll/common', listViews.allCommon, name="allCommon"),
    path('listAll/cpf', listViews.allCpf, name="allCpf"),
    path('listAll/cnpj', listViews.allCnpj, name="allCnpj"),
    path('listAll/segment', listViews.allSegment, name="allSegment"),
    path('listAll/gender', listViews.allGender, name="allGender"),
    path('listAll/civil', listViews.allCivil, name="allCivil"),
    path('listOne/common/<int:common_user_id>', listViews.oneCommon, name='oneCommon'),
    path('listOne/cnpj/<int:user_cnpj_id>', listViews.oneCnpj, name='oneCommon'),
    path('listOne/cpf/<int:user_cpf_id>', listViews.oneCpf, name='oneCommon'),
    path('listCity/perState/<str:state>', listViews.cityPerState, name='cityPerState'),

    path('create/cnpj', createViews.createCnpj, name="createCnpj"),
    path('create/cpf', createViews.createCpf, name="createCpf")
]