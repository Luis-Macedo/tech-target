from django.urls import path
from . import listViews
from . import cnpjViews
from . import cpfViews

urlpatterns = [
    path('listAll/common', listViews.allCommon, name="allCommon"),
    path('listAll/cpf', listViews.allCpf, name="allCpf"),
    path('listAll/cnpj', listViews.allCnpj, name="allCnpj"),
    path('listAll/segment', listViews.allSegment, name="allSegment"),
    path('listAll/gender', listViews.allGender, name="allGender"),
    path('listAll/civil', listViews.allCivil, name="allCivil"),
    path('listOne/cnpj/<int:user_cnpj_id>', cnpjViews.oneCnpj, name='oneCommon'),
    path('listOne/cpf/<int:user_cpf_id>', cpfViews.oneCpf, name='oneCommon'),
    path('listCity/perState/<str:state>', listViews.cityPerState, name='cityPerState'),

    path('create/cnpj', cnpjViews.createCnpj, name="createCnpj"),
    path('create/cpf', cpfViews.createCpf, name="createCpf")
]