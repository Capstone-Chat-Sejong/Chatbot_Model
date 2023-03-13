# Chatbot_Model
2023 캡스톤 챗봇 모델


## pretrained model
### CHATBOT

- **kogpt2(skt)**  : https://github.com/SKT-AI/KoGPT2
- **kogpt(kakaobrain)** :  https://github.com/kakaobrain/kogpt

일상 대화 모델은 kogpt 모델로 개발 예정. 


### CLASSIFIER(or Keyword)

- **KoBERT(skt)** : https://github.com/SKTBrain/KoBERT
(+ https://github.com/monologg/KoBERT-Transformers)
- **DistilKoBERT** : https://github.com/monologg/DistilKoBERT

세종대 관련 정보와 일상대화를 나누는 기준을 명확하게 세우진 않았지만 classification을 진행할때 KoBERT 모델을 사용하게 되면 사용 예정 모델들. or Keyword를 Question에서 바로 가져와서 주제별로 바로 답변할 수 있도록 하는 방법도 고려중.

<br/>

## Data Collection
- 깃허브 chatbot dataset https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv (11823 pair)
- 모두의 말뭉치 / AI-hub 온라인대화 일상대화 data (?로 끝나는 질문과 가까운 시간안에 대답하는 질문답변 pair - 고려중)


<br/>


## Sejong Univ.
세종대 관련 주제 - 세분화

<br/>
  
## Scoring Methods
정량 / 정성 평가 지표

<br/>


