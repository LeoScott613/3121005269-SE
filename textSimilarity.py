from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer

origin_file=open("orig.txt",mode="r",encoding="utf8")
copy_file=open("orig_add.txt",mode="r",encoding="utf8")

origin_text=origin_file.read()
copy_text=copy_file.read()

print(origin_text)
print(copy_text)

list_origin_text=[origin_text]
list_copy_text=[copy_text]

st_model=SentenceTransformer("./paraphrase-multilingual-MiniLM-L12-v2")
origin_embedding=st_model.encode(list_origin_text)
copy_embedding=st_model.encode(list_copy_text)# 嵌入式文本是由模型创建的，而sentenceTransformer仅用于读取模型

cosine_value=cos_sim(origin_embedding,copy_embedding)

print ("二者的文本相似度",cosine_value.item()*100,"%")