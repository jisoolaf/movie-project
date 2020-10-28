# API 파일 개수 제한으로 여러개의 csv를 만든이후 하나로 합친 코딩

import csv
import glob
import os

input_path = r'C:\Users\DELL\eclipse-workspace\HomeTraining\Home' # 파일들을 불러올 디렉터리 경로
output_path = r'C:\Users\DELL\eclipse-workspace\HomeTraining\Home\kobisapiresultt.csv' # 하나로 합칠 파일명

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'imsi0*')): # csv파일들과 주소를 결합하여 파일을 불러온다
    print(os.path.basename(input_file)) # 불러온 파일명을 print해서 확인할 수 있게 한다
    with open(input_file, 'r', encoding='utf-8', newline='') as csv_in_file: # 불러온 csv파일을 연다
        with open(output_path, 'a', encoding='utf-8', newline='') as csv_out_file: # 합칠 csv파일을 'a'로 해서 연다
            filereader = csv.reader(csv_in_file) # csv.reader()로 읽은 내용을 filereader에 저장한다
            filewriter = csv.writer(csv_out_file)
            if first_file: # 첫번째 파일의 경우, header와 같이 복사되도록 한다
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False # 복사가 끝나면 첫번째 파일이 아니기 때문에 False로 명명한다
            else:
                header = next(filereader) # 첫번째 파일이 아닐경우, 머릿글을 header에 저장한다
                for row in filereader:
                    filewriter.writerow(row) # header를 제외하고 읽은 내용을 쓴다(이때 붙여진 내용은 이전 내용과 띄어쓰기 없이 붙여진다
                    