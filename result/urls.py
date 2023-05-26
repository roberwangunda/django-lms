from django.urls import path
from .views import (
    add_score, add_score_for, grade_result, assessment_result, 
    course_registration_form, result_sheet_pdf_view
)

from result.views import ResultListView, create_result, edit_results   

urlpatterns = [
    path('manage-score/', add_score, name='add_score'),
    path('manage-score/<int:id>/', add_score_for, name='add_score_for'),
    
    path('grade/', grade_result, name="grade_results"),
    path('assessment/', assessment_result, name="ass_results"),

	path('result/print/<int:id>/', result_sheet_pdf_view, name='result_sheet_pdf_view'),
	path('registration/form/', course_registration_form, name='course_registration_form'),
    
    path("create/", create_result, name="create-result"),
    path("edit-results/", edit_results,  name="edit-results"),
    path("view/all", ResultListView.as_view(), name="view-results"),
]
