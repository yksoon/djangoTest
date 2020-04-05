# 필요한 파일 import
from PyPDF2 import PdfFileReader, PdfFileWriter
import os, zipfile, shutil


class PDF_treat:
    def __init__(self, file_path, output_path=os.getcwd()):
        self.complete_file = None   # 완료파일
        self.file_path = file_path  # 타겟 경로
        self.target_path, tail = os.path.split(file_path)   # 타겟이 위치한 폴더의 경로
        self.fname = os.path.splitext(tail)[0]  # 타겟의 파일명(확장자 제외)
        self.ouput_path = output_path   # 결과물
        self.pdf_list = []          # pdf 파일명 리스트

    # PDF들을 쪼갬    
    def split_pdf(self):
        pdf = PdfFileReader(self.file_path)
        path = f'{self.target_path}\\{self.fname}\\'
        self.make_dirs(path + '\\')
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))

            output_filename = f'{path}{self.fname}_page_{page+1}.pdf'
            self.pdf_list.append(f'{self.fname}_page_{page+1}.pdf')

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
            
        self.complete_file = self.zip_pdf(path, self.pdf_list)
        return self.complete_file

    def merge_pdf(self):
        pass

    # PDF들을 압축 함
    def zip_pdf(self, pdf_foler_path, *args):
        os.chdir(pdf_foler_path)
        self.make_dirs(self.ouput_path + '\\')
        filezip = zipfile.ZipFile(self.ouput_path + '\\' + self.fname + '.zip', 'w')

        for afile in args[0]:
            filezip.write(afile, compress_type=zipfile.ZIP_DEFLATED)
        
        filezip.close()
        os.chdir(self.ouput_path)
        return filezip


    def unzip_zip(self):
        pass

    # 지정 경로 하부의 모든것을 삭제
    def remove_etc(self):
        shutil.rmtree(f'{self.target_path}\\{self.fname}\\')
    
    # 지정 경로까지 폴더를 생성
    def make_dirs(self, path):
        try:
            os.makedirs(path)
        except FileExistsError:
            pass

if __name__ == '__main__':
    input_path = r"/Users/yong-kwangsoon/Desktop/YKS_project/djangoProject/secondTest/handlepdf/pdf_sample.pdf"
    output_path = r"/Users/yong-kwangsoon/Desktop/YKS_project/djangoProject/secondTest/uploads"
    nadure = PDF_treat(input_path, output_path)
    nadure.split_pdf()
    print(nadure.complete_file.filemane)
    nadure.remove_etc()



