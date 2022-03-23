from bs4 import BeautifulSoup 
#BeautifulSoup은 html 및 xml 문서의 구문 분석을 하기 위한 python 패키지

from urllib.request import urlopen

import re
# \n, \t. " "을 지우는 기능 사용 위해서 가져옴

with urlopen('https://www.bomtoon.com/main/rank?type=99') as response:
    #response=urlopen('사이트 링크') 과 동일한 기능
    soup = BeautifulSoup(response, 'html.parser') #, from_encoding='utf-8'
    
    f = open("봄툰_웹툰_순위.txt", 'w', encoding='utf-8')
    #txt 저장 시 한글 깨짐 현상 방지 위해 encoding='utf-8' 추가
    
    list=soup.select(".cont > p") 
    #select 함수는 리스트 타입 반환
    #class="cont"의 자식들 중 태그가 p인 애들을 모두 긁어와서 저장    
        
    for i in range(len(list)) :
        if (i%3!=0) :
            continue
        data=list[i].get_text() #태그 부분 삭제
        title=re.sub('\s+',' ',data) #공백 부분 삭제
        f.write( title+"\n" ) #파일 저장
        
f.close()
        
#좀 더 세부적인 부분을 선택하는 것에 대해서는
#공식문서 참고 추천
#span 태그 안에 class-ah_k인 것을 선택하고자 한다면
#soup.select("span.ah_k")

#.get을 통해 태그 부분을 제외 가능
#print(anchor.get_text());

#텍파로 저장하는 방법
