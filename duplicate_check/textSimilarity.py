# import cProfile
from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer

def main():
    origin_file=open(".\data_set\orig.txt",mode="r",encoding="utf8")
    copy_file1=open(".\data_set\orig_0.8_add.txt",mode="r",encoding="utf8")
    copy_file2=open(".\data_set\orig_0.8_del.txt",mode="r",encoding="utf8")
    copy_file3=open(".\data_set\orig_0.8_dis_1.txt",mode="r",encoding="utf8")
    copy_file4=open(".\data_set\orig_0.8_dis_10.txt",mode="r",encoding="utf8")
    copy_file5=open(".\data_set\orig_0.8_dis_15.txt",mode="r",encoding="utf8")

    origin_text=origin_file.read()
    copy_text1=copy_file1.read()
    copy_text2=copy_file2.read()
    copy_text3=copy_file3.read()
    copy_text4=copy_file4.read()
    copy_text5=copy_file5.read()

    # print(origin_text)
    # print(copy_text1)

    list_origin_text=[origin_text]
    list_copy_text1=[copy_text1]
    list_copy_text2=[copy_text2]
    list_copy_text3=[copy_text3]
    list_copy_text4=[copy_text4]
    list_copy_text5=[copy_text5]

    # 嵌入式文本是由模型创建的，而sentenceTransformer仅用于读取模型
    st_model=SentenceTransformer("./paraphrase-multilingual-MiniLM-L12-v2")
    origin_embedding=st_model.encode(list_origin_text)
    copy_embedding1=st_model.encode(list_copy_text1)
    copy_embedding2=st_model.encode(list_copy_text2)
    copy_embedding3=st_model.encode(list_copy_text3)
    copy_embedding4=st_model.encode(list_copy_text4)
    copy_embedding5=st_model.encode(list_copy_text5)

    cosine_value1=cos_sim(origin_embedding,copy_embedding1)
    cosine_value2=cos_sim(origin_embedding,copy_embedding2)
    cosine_value3=cos_sim(origin_embedding,copy_embedding3)
    cosine_value4=cos_sim(origin_embedding,copy_embedding4)
    cosine_value5=cos_sim(origin_embedding,copy_embedding5)

    print ("orig_0.8_add和orig的文本相似度",cosine_value1.item()*100,"%")
    print ("orig_0.8_del和orig的文本相似度",cosine_value2.item()*100,"%")
    print ("orig_0.8_dis_1和orig的文本相似度",cosine_value3.item()*100,"%")
    print ("orig_0.8_dis_10和orig的文本相似度",cosine_value4.item()*100,"%")
    print ("orig_0.8_dis_15和orig的文本相似度",cosine_value5.item()*100,"%")

# cProfile.run("main()")
main()