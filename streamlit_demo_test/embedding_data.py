# KR-SBERT 라이브러리 사용
# 해당 모델을 사용하여 임베딩 데이터 저장(속도 개선을 위한)

import pandas as pd
from tqdm import tqdm
import torch
from sentence_transformers import SentenceTransformer

tqdm.pandas()

train_file = "/Users/Home/Documents/GitHub/Chatbot4Univ/train_tools/qna/train_data.xlsx"
model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

df = pd.read_csv(train_file, encoding = 'cp949')
df['embedding_vector'] = df['질문'].progress_map(lambda x : model.encode(x))
df.to_csv("train_data_embedding.csv", index=False)

embedding_data = torch.tensor(df['embedding_vector'].tolist())
torch.save(embedding_data, 'embedding_data.pt')

'''
class create_embedding_data:
    def __init__(self, preprocess, df):

        self.p = preprocess
        self.df = df
        self.model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

    def create_pt_file(self):
        target_df = list(self.df['질문'])

        for i in range(len(target_df)):
            sentence = target_df[i]
            pos = self.p.pos(sentence)
            keywords = self.p.get_keywords(pos, without_tag=True)
            temp = ""
            for k in keywords:
                temp += str(k)
            target_df[i] = temp

        self.df['질문 전처리'] = target_df
        self.df['embedding_vector'] = self.df['질문 전처리'].progress_map(lambda x : self.model.encode(x))
        self.df.to_csv("train_data_embedding.csv", index=False)
        embedding_data = torch.tensor(self.df['embedding_vector'].tolist())
        torch.save(embedding_data, './train_tools/qna/embedding_data.pt')
'''