query_embedding

질문 입력  
질문 전처리  

해당 질문 임베딩    
sentence_bert -> cosine similarity로 가장 유사한 문장 찾음   
konlpy -> nouns에서 핵심어 추출 (전달률 측정)
두가지 값의 정확도를 합산한 값중에서 가장 높은 질문 채택 후 답변 출력

질의 응답 csv에서 가장 유사한 질문 찾고 답변 출력.  

streamlit으로 데모사이트 만들어서 시간 얼마나 걸리는지 측정 예정   
(+ 수강이수표같은 사진도 출력~~)
