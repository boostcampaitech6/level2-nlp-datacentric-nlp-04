import pandas as pd
import re


end = ['종합', r'\d보', r'종합\d보']
start = ['그래픽', '특징주', '게시판', '주말 N 여행', '주마 레 녀행', '위클리 스마트', '1보', '2보']

def remove_starting_with(text, start_chars):
    for char in start_chars:
        text = re.sub(r'\b' + char + r'\w*\b', '', text)
    return text.strip()


def remove_ending_with(text, end_chars):
    for char in end_chars:
        text = re.sub(r'\b\w*' + char + r'\b', '', text)
    return text.strip()

# ['…', '·', '...', '↔', '↓']
def remove_unk(text):
    return re.sub(r'\…|\·|\.\.\.|\↔|\↓', ' ', text)


df = pd.read_csv('../data/train.csv')

df_unk = df.copy(deep=True)
df_start_end = df.copy(deep=True)
df_unk_start_end = df.copy(deep=True)


df_unk['text'] = df_unk['text'].apply(lambda x: remove_unk(x))
df_start_end['text'] = df_start_end['text'].apply(lambda x: remove_starting_with(x, start))
df_start_end['text'] = df_start_end['text'].apply(lambda x: remove_ending_with(x, start))
df_unk_start_end['text'] = df_unk_start_end['text'].apply(lambda x: remove_unk(x))
df_unk_start_end['text'] = df_unk_start_end['text'].apply(lambda x: remove_starting_with(x, start))
df_unk_start_end['text'] = df_unk_start_end['text'].apply(lambda x: remove_ending_with(x, start))


df_unk.to_csv('../data/train_unk.csv', index=False)
df_start_end.to_csv('../data/train_start_end.csv', index=False)
df_unk_start_end.to_csv('../data/train_unk_start_end.csv', index=False)