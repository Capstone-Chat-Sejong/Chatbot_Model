query_embedding

질문 입력  
질문 전처리  

해당 질문 임베딩    
sentence_bert -> cosine similarity로 가장 유사한 문장 찾음   
konlpy -> nouns에서 핵심어 추출 (전달률 측정)
두가지 값의 정확도를 합산한 값중에서 가장 높은 질문 채택 후 답변 출력

질의 응답 csv에서 가장 유사한 질문 찾고 답변 출력.  

streamlit으로 데모사이트 만들어서 시간 얼마나 걸리는지 측정 예정   
(+ 수강이수표같은 사진도 출력)

TF-IDF, LDA같은 기법들 많이 사용해보려했으나 챗봇의 모델의 기본적 특성으로 인해
문답 질문들이 짧음. 따라서 핵심어 추출 명사, 동사정도만 해도 충분해보임.



<br/>

### 메모장
text = re.sub('RT @[\w_]+: ', '', text)

enticons 제거
text = re.sub('@[\w_]+', '', text)

URL 제거
text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ' ', text) # http로 시작되는 url
text = re.sub(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", ' ', text) # http로 시작되지 않는 url

Hashtag 제거
text = re.sub('[#]+[0-9a-zA-Z_]+', ' ', text)

쓰레기 단어 제거
text = re.sub('[&]+[a-z]+', ' ', text)

특수문자 제거
text = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]', ' ', text)

특정 문자 제거
for i in ['!','@','#','*'] :
    new_id = new_id.replace(i, "")

띄어쓰기 제거
text = text.replace('\n',' ')

if Num is True:
숫자 제거
text = re.sub(r'\d+',' ',text)

영어 제거 
text = re.sub('[a-zA-Z]' , ' ', text)

대문자로 변환
text = text.upper()

소문자로 변환
text = text.lower()
정리
text = ' '.join(text.split())
