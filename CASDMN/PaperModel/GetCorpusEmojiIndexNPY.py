# coding="utf-8"

import numpy as np

Parent_File_Path="/home/code_as_poetry/corpus_60000/"
All_Emoji_List_Path = Parent_File_Path+"All_Emoji_List.npy"

Adjust_Pos_Emoji_File_Path = Parent_File_Path+"Ad_Pos_Emoji.txt"
Adjust_Neg_Emoji_File_Path = Parent_File_Path+"Ad_Neg_Emoji.txt"

Pos_Emoji_Index_List_Path = Parent_File_Path+"Pos_Emoji_Index.npy"
Neg_Emoji_Index_List_Path = Parent_File_Path+"Neg_Emoji_Index.npy"

Total_number = 60000

if __name__=="__main__":
    print("GetCorpusEmojiIndexNPY Main")

    All_Emoji_List = list(np.load(All_Emoji_List_Path))
    print(type(All_Emoji_List))
    Adjust_Pos_Emoji_File = open(Adjust_Pos_Emoji_File_Path,"r")
    Adjust_Neg_Emoji_File = open(Adjust_Neg_Emoji_File_Path,"r")

    Adjust_Pos_Emoji_Index_List=[]
    Adjust_Neg_Emoji_Index_List=[]

    for i in range(Total_number):
        the_sample_emojis_str = Adjust_Pos_Emoji_File.readline()
        the_sample_emojis_list = the_sample_emojis_str.split(" ")
        temp_list=[]
        for j in range(len(the_sample_emojis_list)):
            if "\n" in the_sample_emojis_list[j]:
                the_sample_emojis_list[j] = the_sample_emojis_list[j][0:-1]
            if the_sample_emojis_list[j]!="":
                temp_list.append(All_Emoji_List.index(the_sample_emojis_list[j]))

        Adjust_Pos_Emoji_Index_List.append(temp_list)

    for i in range(Total_number):
        the_sample_emojis_str = Adjust_Neg_Emoji_File.readline()
        the_sample_emojis_list = the_sample_emojis_str.split(" ")
        temp_list=[]
        for j in range(len(the_sample_emojis_list)):
            if "\n" in the_sample_emojis_list[j]:
                the_sample_emojis_list[j] = the_sample_emojis_list[j][0:-1]
            if the_sample_emojis_list[j]!="":
                temp_list.append(All_Emoji_List.index(the_sample_emojis_list[j]))

        Adjust_Neg_Emoji_Index_List.append(temp_list)


    print("Adjust_Pos_Emoji_Index_List",len(Adjust_Pos_Emoji_Index_List))
    print("Adjust_Neg_Emoji_Index_List",len(Adjust_Neg_Emoji_Index_List))
    print(Adjust_Pos_Emoji_Index_List[1],All_Emoji_List[Adjust_Pos_Emoji_Index_List[1][0]])
    print(Adjust_Neg_Emoji_Index_List[3],All_Emoji_List[Adjust_Neg_Emoji_Index_List[3][7]])


    # run one time
    # np.save(Pos_Emoji_Index_List_Path,Adjust_Pos_Emoji_Index_List)
    # np.save(Neg_Emoji_Index_List_Path,Adjust_Neg_Emoji_Index_List)