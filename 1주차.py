import pandas as pd

dict_data = {'a':1, 'b':2, 'c':3}#딕셔너리 선언

sr = pd.Series(dict_data)#series 메서드 : dictionary를 series로 변환

print(type(sr))
print('n')
print(sr)

import pandas as pd

list_data = ['123', 3.14, "ABC", 100, True] 
sr = pd.Series(list_data)#list를 series로 변환
print(sr)

import pandas as pd

tup_data = ('a', '200', True, 3.14)
sr = pd.Series(tup_data, index=['A', 'B','C', 'D'])#tuple을series로, index에 이름 부여.
print(sr)

import pandas as pd

tup_data = ('a', '200', True, 3.14)
sr = pd.Series(tup_data, index=['A', 'B','C', 'D'])#tuple을series로, index에 이름 부여.
print(sr)
print(sr[0])
print(sr['A'])
print(sr[1:3])#index번호 1,2,3 호출
print(sr['A','C'])#a ~ c 까지의 index


#1-4
import pandas as pd

dict_data = {'c0':[1,2,3],'c1':[1,2,4], 'c2':[1,6,3], 'c3':[6,2,3]}
df = pd.DataFrame(dict_data)#dictionary 자료형을 dateframe으로 변환
print(type(df))
print('\n')
print(df)

#1-5
import pandas as pd

df = pd.DataFrame([[1,2,3],[1,2,4]], 
                  index = ['A','B'], 
                  columns = ['1st','2nd','3rd'])#행과 열에 이름을 지정하여 데이터 프레임 만들기

print(type(df))
print('\n')
print(df)

df.index = ['X','Y']
df.columns = ['1','2','3']
print(type(df))
print('\n')
print(df.index)
print('\n')
print(df.columns)

#1-6
import pandas as pd
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])

print(df)
print('\n')

df.rename(columns={'나이':'연령', '성별':'남여', '학교':'소속'}, inplace=True)#열 이름을 변경, :앞이 변경전, 뒤가 변경 후
df.rename(index={'준서':'학생1', '예은':'학생2' }, inplace=True)#행 이름을 변경
print(df)

#1-7,8
import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])#dictionary를 dateframe으로.
print(df)
print('\n')

df2 = df[:]#df를 복사하여 df2에 저장
df2.drop('우현', inplace=True)#df2는 df1에서 우현의 row를 제거한 것
print(df2)
print('\n')

df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True)#axis는 축 옵션, 0일 때 행을 삭제, 1일 때 열을 삭제

df4 = df[:]
df4.drop('수학', axis=1, inplace=True)#수학에 해당하는 열을 삭제, 열을 삭제할 땐 axis=1을 작성해야한다.
print(df4)
print('\n')

df5=df[:]
df5.drop(['영어','음악'], axis =1, inplace=True )
print(df5)

#1-9 슬라이싱 - 행 선택
import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])#dictionary를 dateframe으로.
print(df)
print('\n')

labell = df.loc['서준']#이름 기반으로 행 선택
positional = df.iloc[0]#정수형 index 기반으로 행 선택
print(labell)
print('\n')
print(positional)

labell2 = df.loc[['서준', '우현']]#이름 기반으로 각 각 2개의 행 선택
positional2 = df.iloc[[0,1]]#정수형 index기반으로 각 각 2개의 행 선택
print(labell2)
print('\n')
print(positional2)

labell3 = df.loc['서준':'우현']#이름기반으로 범위를 지정할 때 마지막 값이 포함된다.
positional3 = df.iloc[0:1]#index 기반으로 범위를 지정할 때는 마지막 값이 제외된다.
print(labell3)
print('\n')
print(positional3)

#1-10 슬라이싱 - 열 선택
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))#자료형은 dataframe이다 
print('\n')

math1 = df['수학']#수학에 해당하는 열 데이터만 선택하여 math1이라는 변수에 저장한다.
print(math1)
print(type(math1))#자료형은 series이다. 
print('\n')

eng = df.영어
print(eng)
print(type(eng))

music_pe = df[['음악','체육']]
print(music_pe)
print(type(music_pe))
print('\n')

math2 = df[['수학']]
print(math2)
print(type(math2))

#슬라이싱

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.iloc[ : :2 ]#처음부터 끝까지 슬라이싱 간격을 2로 하여 행을 선택한다

df.iloc[0:3:2]

df.iloc[ : :-1]#역순으로 행 선택하기

#1-11 원소 선택

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)#set_index메서드 -> 이름 열을 새로운 행 인덱스로 지정한다

print(df)
print('\n')
a = df.loc['서준', '음악']#이름 기반 위치에서, 서준 행의 음악 열에 해당하는 원소
print(a)
print('\n')

b = df.iloc[0,2]#index기반 위치에서, 1번째 행의 3번째 열에 해당하는 원소
print(b)
print('\n')

c= df.loc['서준',['음악','체육']]
print(c)
print('\n')

d = df.iloc[0,[2,3]]
print(d)

e = df.loc['서준', '음악':'체육']#서준 행에서 음악부터 체육에 해당하는 범위의 원소
print(e)
print('\n')

f = df.iloc[0,2: ]#1번째 행에서 3번째 열부터 끝 열까지의 범위에 해당하는 원소
print(f)
print('\n')

g = df.loc[['서준', '우현'], ['음악', '체육']]#
print(g)
print('\n')

h = df.iloc[[0, 1], [2, 3]]#
print(h)
print('\n')

i = df.loc['서준':'우현', '음악':'체육']#이름 기반 범위 지정(끝값 포함)
print(i)
print('\n')

j = df.iloc[0:2, 2:]#index기반 범위 지정(끝 값 미포함)
print(j)

#1-12 열 추가 
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df['국어'] = 80 #새로운 열 추가, 모든 국어열의 값이 80
print(df)

#1-13 행 추가
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.loc[3] = 0 #새로운 행 추가 : 4번째 행의 모든 값이 0
print(df)
print('\n')

df.loc[4] = ['동규',90,80,70,60] #새로운 행 추가 : 배열 형태로 행을 추가한다
print(df)
print('\n')

df.loc['5행'] = df.loc[3]#기존 행을 복사해서 추가한다
print(df)

#1-14 원소의 값 변경

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)#이름 열을 새로운 인덱스로 지정하고 df객체에 변경사항 반영
print(df)
print('\n')

df.iloc[0][3] = 80 #1번째 행, 4번째 열의 원소를 80으로 바꾼다
print(df)
print('\n')

df.iloc[0][3] = 80
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준', '체육'] = 100
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 50 #여러개의 원소의 값을 바꾼다
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)

#1-15 행과 열 바꾸기 (전치시키기)
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df = df.transpose()#dataframe을 전치시키려면 기존 객체에 새로운 객체를 할당시켜줘야 한다
print(df)
print('\n')

df = df.T#다른 방법
print(df)

#1-16 특정 열을 행 인덱스로 설정하기

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data) #dictionary를 dataframe으로
print(df)
print('\n')

ndf = df.set_index(['이름'])#특정 열을 행 index로 설정하기
print(ndf)
print('\n')

ndf2 = ndf.set_index('음악')
print(ndf2)
print('\n')

ndf3 = ndf.set_index(['수학','음악'])
print(ndf3)

#1-17 행 인덱스 재배열

import pandas as pd
#dictionary지정
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])#dictionary를 dateframe으로, 행의 이름을 지정
print(df)
print('\n')

new_index = ['r0','r1','r2','r3','r4'] #새로운 index의 list
ndf = df.reindex(new_index)#새로운 index를 위의 list로 지정
print(ndf)#새로운 list의 값이 채워지지 않았기 때문에 Nan으로 표시된다
print('\n')

new_index = ['r0','r1','r2','r3','r4'] #새로운 index의 list
ndf2 = df.reindex(new_index, fill_value=0)#Nan값을 0으로 채운다
print(ndf2)
print('\n')

#1-18정수형 위치 인덱스로 초기화

import pandas as pd
#dictionary지정
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])#dictionary를 dateframe으로, 행(index)의 이름을 지정
print(df)
print('\n')

ndf = df.reset_index()#이름이 지정된 행을 정수형으로 초기화하는 메서드
print(ndf)

#1-19,20 정렬
import pandas as pd

# 딕셔서리를 정의
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

ndf = df.sort_index(ascending=False)#내림차순으로 행index 정렬, false는 내림차순, True는 오름차순
print(ndf)

ndf2 = df.sort_index(by='c1', ascending=False)#c1 열의 값을 기준으로 행index들이 내림차순으로 정렬된다.
print(ndf2)

#1-21 시리즈 산술 연산
import pandas as pd

#dictionary를 series로
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
print('\n')

percen = student1/200#series의 모든 값을 200으로 나눈다
print(percen)
print('\n')
print(type(percen))#실수형 자료

#1-22
import pandas as pd

stu1 = pd.Series({'국어':100, '영어':80, '수학':90})
stu2 = pd.Series({'수학':80, '국어':90, '영어':80})

print(stu1)
print('\n')
print(stu2)
print('\n')

#series 끼리의 산술연산 : 같은 위치에서 산술연산이 이루어진다
add = stu1 + stu2
sub = stu1 - stu2
mult = stu1 * stu2
div = stu1/stu2
print(type(div))

res = pd.DataFrame([add, sub, mult, div], index=['+','-','*','/'])
print(res)


#1-23 nan값이 있을 때 연산
import pandas as pd
import numpy as np

stu1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})#numpy 라이브러리에서 nan값 가져오기
stu2 = pd.Series({'수학':80, '국어':90})

print(stu1)
print('\n')
print(stu2)
print('\n')

add = stu1 + stu2 #nan과 어떤 정수를 더하면 0+정수 라고 생각하기 쉽지만, 그렇지 않음에 주의!
sub = stu1 - stu2
mult = stu1 * stu2
div = stu1/stu2

print(type(div))
print('\n')


result = pd.DataFrame([add, sub, mult, div], 
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)#nan을 포함한 연산은 모두 nan으로 처리한다.

#1-24 연산 메서드 : 공통 index가 없거나 nan이 포함된 경우 nan이 반환되는 것을 방지하기 위한 메서드

import pandas as pd
import numpy as np

stu1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})#numpy 라이브러리에서 nan값 가져오기
stu2 = pd.Series({'수학':80, '국어':90})

print(stu1)
print('\n')
print(stu2)
print('\n')

sr_add = stu1.add(stu2, fill_value=0)
sr_sub = stu1.add(stu2, fill_value=0)
sr_mult = stu1.mul(stu2, fill_value=0)#영어라는 공통 index가 없으면 그 자리에 0을 넣어서 연산한다
sr_div = stu1.div(stu2, fill_value=0) #0으로 나누면 inf가 반환된다

res = pd.DataFrame([sr_add,sr_sub, sr_mult, sr_div], index=['덧셈','뺄셈', '곱셈', '나눗셈'])
print(res)

#1-25 데이터프레임에 숫자 더하기

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')#seaborn 라이브러리에 내장되어 있는 데이터
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.tail())          #마지막 5행을 표시
print('\n')
print(type(df))
print('\n')
 
addition = df + 10
print(addition.tail())    #마지막 5행을 표시
print('\n')
print(type(addition))
print('\n')

subtraction = addition - df
print(subtraction.tail())   #마지막 5행을 표시
print('\n')
print(type(subtraction))

#2-1 csv파일 읽기
# 파일의 경로를 하나의 변수에 저장한다. /와\를 잘 구분해야 함.

import pandas as pd


file_path = 'C:/Users/user/Desktop/물리학 프로그래밍/05000266/part2/read_csv_sample.csv'

df1 = pd.read_csv(file_path)#csv파일을 dataframe으로 저장
print(df1)
print('\n')


df2 = pd.read_csv(file_path, header=None)#header옵션이 없으면 첫 행이 열 이름이 된다.
print(df2)
print('\n')


df3 = pd.read_csv(file_path, index_col=None)#index column옵션이 없으면 자동으로 정수형 인덱스가 지정된다
print(df3)
print('\n')


df4 = pd.read_csv(file_path, index_col='c0') #c0열이 index column이 된다
print(df4)

#2-2 엑셀 읽기

import pandas as pd


file_path = 'C:/Users/user/Desktop/물리학 프로그래밍/05000266/part2/남북한발전전력량.xlsx'
df1 = pd.read_excel(file_path, engine='openpyxl')# header=0 기본 옵션
df2 = pd.read_excel(file_path, engine='openpyxl', 
                    header=None)  # header=None 옵션

# 데이터프레임 출력
print(df1)
print('\n')
print(df2)

#2-3jason 파일
import pandas as pd

# read_json() 함수로 데이터프레임 변환 
df = pd.read_json('C:/Users/user/Desktop/물리학 프로그래밍/05000266/part2/read_json_sample.json')  
print(df)
print('\n')
print(df.index)

#2-4 웹에서 가져오기

import pandas as pd

# HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url ='C:/Users/user/Desktop/물리학 프로그래밍/05000266/part2/sample.html'

tables = pd.read_html(url)#웹페이지 주소를 읽어 dataframe으로

print(len(tables))# 표의 갯수 확인
print('\n')

for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')

df = tables[1] 

df.set_index(['name'], inplace=True)
print(df)

#2-5 bs4로 받은 객체를 pandas로 처리하기 

import requests #request 모듈
from bs4 import BeautifulSoup as bs #beautifulsoup모듈
import pandas as pd 

page = requests.get("https://library.gabia.com/") #get 메서드 : 해당 url의 html을 요청받을 수 있다
soup = bs(page.text, "html.parser") #응답받은 html내용을 beautifulsoup객체로 반환한다 

elements = soup.select('div.esg-entry-content a.eg-grant-element-0')#html에서 esg-entry-content태그의 하위에 존재하는 a 태그 하위의 span 태그를 선택한다

titles = [] #빈 리스트 
links = []
for index, element in enumerate(elements, 1): #enumerate함수 : index와 원소에 동시에 접근하며 for문 돌리기 ->index와 원소로 이루어진 튜플을 반환한다 
        titles.append(element.text)
        links.append(element.attrs['href']) #attrs메서드 : href에 해당하는 클래스(링크)를 반환


df = pd.DataFrame()
df['titles'] = titles
df['links'] = links

#df.to_excel('./library_gabia.xlsx', sheet_name='Sheet1')#데이터프레임을 엑셀로

print(df)