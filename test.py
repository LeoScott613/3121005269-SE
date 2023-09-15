from sentence_transformers.util import cos_sim  
from sentence_transformers import SentenceTransformer as SBert

st_model=SBert("./paraphrase-multilingual-MiniLM-L12-v2")
cn_sentence1=['今天吃吮指原味鸡']
cn_sentence2=['今天我吃了吮指原味鸡']

embeddings1=st_model.encode(cn_sentence1)
embeddings2=st_model.encode(cn_sentence2)
cosine_score=cos_sim(embeddings1,embeddings2)

print ("文本相似度",cosine_score.item()*100,"%")