from django.shortcuts import render

from django import forms
from .models import merge_pdfs, split_pdf
from django.views.generic.edit import FormView
from handlepdf.pdf_handle import PDF_treat
from django.conf import settings

# Create your views here.

# 폼 생성
class merge_form(forms.ModelForm):
    class Meta:
        model = merge_pdfs
        exclude = ('completed_file',)  # completed_file 필드를 제외

class split_form(forms.ModelForm):
    class Meta:
        model = merge_pdfs
        exclude = ('completed_file',)  # completed_file 필드를 제외


# 뷰 생성
class MergeView(FormView):
    template_name = 'handlepdf/form_temp.html'
    form_class = merge_form
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class SplitView(FormView):
    template_name = 'handlepdf/form_temp.html'
    form_class = split_form
    success_url = '/'

    def form_valid(self, form):
        form.save()     # 일단 폼을 세이브해서 파일을 저장하고,

        origin_file_path = form.instance.origin_file_path       # 원본파일 경로를 받아온 뒤
        output_path = settings.MEDIA_ROOT+"\\complete\\split\\"

        do_split = PDF_treat(origin_file_path, output_path)
        do_split.split_pdf()
        # 만들어뒀던 클래스에 원본파일 이름과 아웃풋 경로를 넣어줌

        form.instance.completed_file = do_split.complete_file.filename
        form.save()
        # 폼의 인스턴스에서 completed_file 을 작업이 끝난 파일의 이름으로 넣어주고
        # 이를 저장함.

        do_split.remove_etc()
        # 나머지 잔류 파일들 삭제

        return super().form_valid(form)
