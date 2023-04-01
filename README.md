# Chatbot_Model
2023 캡스톤 챗봇 모델


## Pretrained model
#### CHATBOT

- **kogpt2(skt)**  : https://github.com/SKT-AI/KoGPT2
- **kogpt(kakaobrain)** :  https://github.com/kakaobrain/kogpt

일상 대화 모델은 kogpt 모델로 개발 예정. 
GPT 모델이 질문에대한 답변을 generate 하기에 가장 알맞은 모델. 문장 생성에 최적화.

#### CLASSIFIER(or Keyword)

- **KoBERT(skt)** : https://github.com/SKTBrain/KoBERT
(+ https://github.com/monologg/KoBERT-Transformers)
- **DistilKoBERT** : https://github.com/monologg/DistilKoBERT

세종대 관련 정보와 일상대화를 나누는 기준을 명확하게 세우진 않았지만 classification을 진행할때 KoBERT 모델을 사용하게 되면 사용 예정 모델들. or Keyword를 Question에서 바로 가져와서 주제별로 바로 답변할 수 있도록 하는 방법도 고려.
(BERT는 문장의 의미를 추출하는데 강점을 가진 모델. -> classificaiton)


## Data Collection
- 깃허브 chatbot dataset https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv (11823 pair)
- 모두의 말뭉치 / AI-hub 온라인대화 일상대화 data (?로 끝나는 질문과 가까운 시간안에 대답하는 질문답변 pair - 고려중 // 일반 상식, 용도별 목적 대화, 주제별 텍스트 일상 대화)
- Naver ClovaCall 110,000 pair qa dataset(요청함 - 우리 모델에 맞는 데이터인지는 확인해봐야 알듯?)
- (+) 데이터가 너무 없으면 영어로된 챗봇 data는 많아서 번역api 돌려서 써도 괜찮을거 같음)

참고 https://github.com/songys/AwesomeKorean_Data

#### Data Preprocessing
- 답변 문장 종결어미 통일
- 맞춤법 (띄어쓰기 - PyKoSpacing (https://github.com/haven-jeon/PyKoSpacing), naver)
- 불용어 처리
- 정규화

+) 한국어 데이터들이 활용하기에 전처리해야될 부분들이 많이 보여 외국어 데이터 번역 후 학습에 사용하려했음. 번역 api가 생각보다 많은 문장을 번역하기에는 부족함.(확실히 바로 사용하기에 좋은 데이터들이 많이 있긴 함.) 결국에는 한국어 데이터를 사용해야함. question answering에서 문단 제거하고 질문-답변 쌍만 꺼내서 이용하는 방법도 생각해봐야 할듯. 아니면 번역기를 만드는건 좀 그런가? 외국인도 사용하는 방향으로?.....

++) 전에 사용되던 대화 데이터들 재검토 중이라 공개 안하는듯. 일단 ai-hub 일반상식, 한국어대화 데이터셋 전처리해서 학습 돌려봐야 할듯.!

## Sejong Univ.
세종대 관련 주제 - 세분화


  
## Scoring Methods
정량 / 정성 평가 지표


## Other Model
#### ChatBot
- KoGPT2 simple chatbot  https://github.com/gyunggyung/KoGPT2-FineTuning
- 키오스크 챗봇  https://github.com/momozzing/kiosk_bot
- KoGPT2-personachat  https://github.com/dreamingjudith/KoGPT2-personachat
- WellnessChatbot for Mental Health  https://github.com/eunjiinkim/WellnessChatbot
- 선물 추천 챗봇  https://github.com/mu0gum/nlp_research


#### kogpt2 model
- 자기소개서 작성 도우미 프로그램  https://github.com/Yngie-C/JasoAI
- 시 생성 모델  https://github.com/newfull5/AI_Poet-KoGPT2
- 공감 답글 생성 모델  https://github.com/jiminAn/Capstone_2022#%ED%8C%80-%EC%9C%84%EB%93%9C%EC%9C%A0-%EC%86%8C%EA%B0%9C


## 주차별 진행상황
#### 3월 2주
 - 주제확정 / 세부 계획 수립
#### 3월 3주
 - chatbot - baseline 코드 완성
 - 학습 데이터 찾기
#### 3월 4주
 - chatbot domain ??
 - chatbot 코드 세분화 (preprocessing / tokenization / train / model test)
 - 학습 데이터 전처리 / 외국어 데이터 활용 방안 탐색    
 #### 3월 5주
 - 질문 임베딩 과정 로직 정의
 - 의도분류 및 해당 답변까지의 출력시간 테스트
 - 학교정보 csv 세분화(제일 중요)

#### 이후 해야될 것들
 - chatbot model finetuning -> wandb sweep


</br>

## Chatbot Structure
![스크린샷 2023-03-27 214539](https://user-images.githubusercontent.com/65898247/229288951-8027070a-7884-48a7-8654-79c99d40ddfb.png)
