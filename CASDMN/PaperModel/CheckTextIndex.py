# coding="utf-8"

import word2vec
import numpy as np

Parent_File_Path="/home/code_as_poetry/corpus_60000/"
Split_Pos_Txt_File_Path=Parent_File_Path+"Ad_Split_Pos_Txt.txt"
Split_Neg_Txt_File_Path=Parent_File_Path+"Ad_Split_Neg_Txt.txt"

Pos_Txt_Index_File_Path=Parent_File_Path+"Pos_Txt_Index.npy"
Neg_Txt_Index_File_Path=Parent_File_Path+"Neg_Txt_Index.npy"

Total_number=60000

ParentFilePath="/home/code_as_poetry/SouGou/"
corpusWord2Vect=ParentFilePath+"corpusWord2Vec.bin"

if __name__=="__main__":

    model = word2vec.load(corpusWord2Vect)

    Split_Pos_Txt_File = open(Split_Pos_Txt_File_Path, "r")
    Split_Neg_Txt_File = open(Split_Neg_Txt_File_Path, "r")

    Pos_List = []
    Neg_List = []

    for i in range(Total_number):
        Pos_List.append(Split_Pos_Txt_File.readline())
        Neg_List.append(Split_Neg_Txt_File.readline())

    Pos_Index_List = np.load(Pos_Txt_Index_File_Path)
    Neg_Index_List = np.load(Neg_Txt_Index_File_Path)

    print("Pos_Index_List",len(Pos_Index_List),Pos_Index_List[1])
    print("Neg_Index_List",len(Neg_Index_List),Neg_Index_List[1])

    str_temp=""
    for i in Neg_Index_List[1]:
        str_temp+=model.vocab[i]

    print(Neg_List[1])
    print(str_temp)