# coding = "utf-8"

import numpy as np
import word2vec

ParentFilePath="/home/code_as_poetry/SouGou/"
corpusWord2Vect=ParentFilePath+"corpusWord2Vec.bin"

Parent_File_Path="/home/code_as_poetry/corpus_60000/"
All_Emoji_Vec_Nd_Path = Parent_File_Path+"All_Emoji_Vec_Nd.npy"

All_Emoji_List_Path = Parent_File_Path+"All_Emoji_List.npy"

Pos_Txt_Index_List_Path=Parent_File_Path+"Pos_Txt_Index.npy"
Neg_Txt_Index_List_Path=Parent_File_Path+"Neg_Txt_Index.npy"

Pos_Emoji_Index_List_Path = Parent_File_Path+"Pos_Emoji_Index.npy"
Neg_Emoji_Index_List_Path = Parent_File_Path+"Neg_Emoji_Index.npy"

if __name__=="__main__":
    print("ProduceSampleIndex_Vec Main")

    model = word2vec.load(corpusWord2Vect)
    All_Emoji_Vec_Nd = np.load(All_Emoji_Vec_Nd_Path)

    All_Emoji_List = np.load(All_Emoji_List_Path)

    Pos_Txt_Index_List = np.load(Pos_Txt_Index_List_Path)
    Pos_Emoji_Index_List = np.load(Pos_Emoji_Index_List_Path)

    Neg_Txt_Index_List = np.load(Neg_Txt_Index_List_Path)
    Neg_Emoji_Index_List = np.load(Neg_Emoji_Index_List_Path)

    # print(type(All_Emoji_Vec_Nd))        # <class 'numpy.ndarray'>
    # print(type(All_Emoji_List))          # <class 'numpy.ndarray'>
    #
    # print(type(Pos_Txt_Index_List))      # <class 'numpy.ndarray'>
    # print(type(Pos_Emoji_Index_List))    # <class 'numpy.ndarray'>
    #
    # print(type(Neg_Txt_Index_List))      # <class 'numpy.ndarray'>
    # print(type(Neg_Emoji_Index_List))    # <class 'numpy.ndarray'>


    The_Sample_Id=59559



    txt_temp = ""
    for i in Neg_Txt_Index_List[The_Sample_Id]:
        txt_temp += model.vocab[i]
    print(txt_temp)

    emoji_temp = ""
    for i in Neg_Emoji_Index_List[The_Sample_Id]:
        emoji_temp += All_Emoji_List[i]
    print(emoji_temp)


    txt_vec_temp = []
    for i in Neg_Txt_Index_List[The_Sample_Id]:
        temp_list = list(model.vectors[i])
        txt_vec_temp.append(temp_list)
    print("txt_vec_temp",type(txt_vec_temp),len(txt_vec_temp),txt_vec_temp)

    emoji_vec_temp=[]
    for i in Neg_Emoji_Index_List[The_Sample_Id]:
        temp_list = list(All_Emoji_Vec_Nd[i])
        emoji_vec_temp.append(temp_list)
    print("emoji_vec_temp",type(emoji_vec_temp),len(emoji_vec_temp),emoji_vec_temp)

    txt_vec_arr = np.array(txt_vec_temp)
    print(txt_vec_arr.shape,txt_vec_arr)

    emoji_vec_arr = np.array(emoji_vec_temp)
    print(emoji_vec_arr.shape, emoji_vec_arr)