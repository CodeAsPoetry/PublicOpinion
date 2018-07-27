# coding:utf-8

import numpy as np

Parent_File_Path="/home/code_as_poetry/corpus_60000/"
Pos_Emoji_File_Path=Parent_File_Path+"Ad_Pos_Emoji.txt"
Neg_Emoji_File_Path=Parent_File_Path+"Ad_Neg_Emoji.txt"

All_Emoji_Path_List = Parent_File_Path+"All_Emoji_List.npy"

Total_number=60000

if __name__=="__main__":

    Pos_Emoji_File = open(Pos_Emoji_File_Path,"r")
    Neg_Emoji_File = open(Neg_Emoji_File_Path,"r")

    AllEmojiList_Error=[]

    Pos_Sample_Emoji=[]
    for i in range(Total_number):
        the_sample_emojis_str=Pos_Emoji_File.readline()
        the_sample_emojis_list = the_sample_emojis_str.split(" ")
        for j in range(len(the_sample_emojis_list)):
            if the_sample_emojis_list[j]==" ":
                continue
            else:
                if "\n" in the_sample_emojis_list[j]:
                    # print(the_sample_emojis_list[j][0:-1])
                    Pos_Sample_Emoji.append(the_sample_emojis_list[j][0:-1])
                else:
                    # print(the_sample_emojis_list[j])
                    Pos_Sample_Emoji.append(the_sample_emojis_list[j])



    Neg_Sample_Emoji=[]
    for i in range(Total_number):
        the_sample_emojis_str=Neg_Emoji_File.readline()
        the_sample_emojis_list = the_sample_emojis_str.split(" ")
        for j in range(len(the_sample_emojis_list)):
            if the_sample_emojis_list[j]==" ":
                continue
            else:
                if "\n" in the_sample_emojis_list[j]:
                    # print(the_sample_emojis_list[j][0:-1])
                    Neg_Sample_Emoji.append(the_sample_emojis_list[j][0:-1])
                else:
                    # print(the_sample_emojis_list[j])
                    Neg_Sample_Emoji.append(the_sample_emojis_list[j])


    print("Pos_Sample_Emoji",len(Pos_Sample_Emoji))
    print("Neg_Sample_Emoji",len(Neg_Sample_Emoji))

    for i in Pos_Sample_Emoji:
        if i not in AllEmojiList_Error:
            AllEmojiList_Error.append(i)

    for i in Neg_Sample_Emoji:
        if i not in AllEmojiList_Error:
            AllEmojiList_Error.append(i)

    print("AllEmojiList_Error",len(AllEmojiList_Error),AllEmojiList_Error)


    AllEmojiList=[]
    for i in AllEmojiList_Error:
        if i!="" and i[0]=="[" and i[-1]=="]":
            AllEmojiList.append(i)

    print("AllEmojiList",len(AllEmojiList),AllEmojiList)
    print("[泪]" in AllEmojiList)

    for i in AllEmojiList_Error:
        if i not in AllEmojiList:
            print(i)

    np.save(All_Emoji_Path_List,AllEmojiList)


    # for i in range(Total_number):
    #     tempstr_p = Pos_Emoji_File.readline()
    #     tempstr_n = Neg_Emoji_File.readline()
    #     templist_p = tempstr_p.split(" ")
    #     templist_n = tempstr_n.split(" ")
    #     for j in range(len(templist_p)):
    #
    #         if templist_p[j] != " ":
    #             # print(templist_p[j])
    #             if "\n" in templist_p[j]:
    #                 # print(templist_p[j][1:-2])
    #                 if "[" in templist_p[j][1:-2]:
    #                     print(i,"P")
    #             else:
    #                 # print(templist_p[j][1:-1])
    #                 if "[" in templist_p[j][1:-1]:
    #                     print(i,"P")
    #
    #     for j in range(len(templist_n)):
    #
    #         if templist_n[j] != " ":
    #             # print(templist_n[j])
    #             if "\n" in templist_n[j]:
    #
    #                 # print(templist_n[j][1:-2])
    #                 if "[" in templist_n[j][1:-2]:
    #                     print(i+1,"N")
    #             else:
    #                 # print(templist_n[j][1:-1])
    #                 if "[" in templist_n[j][1:-1]:
    #                     print(i+1,"N")

    # for i in range(Total_number):
    #     tempstr_p = Pos_Emoji_File.readline()
    #     tempstr_n = Neg_Emoji_File.readline()
    #     if "怒勿忘国耻" in tempstr_p:
    #         print(i,"P")
    #     if "怒勿忘国耻" in tempstr_n:
    #         print(i,"N")











    