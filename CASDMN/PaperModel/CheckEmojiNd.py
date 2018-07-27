# coding="utf-8"

import numpy as np

Parent_File_Path="/home/code_as_poetry/corpus_60000/"
All_Emoji_Vec_Nd_Path = Parent_File_Path+"All_Emoji_Vec_Nd.npy"
All_Emoji_List_Path = Parent_File_Path+"All_Emoji_List.npy"

if __name__=="__main__":
    print("CheckEmojiDict Main")

    All_Emoji_List = np.load(All_Emoji_List_Path)
    All_Emoji_Vec_Nd = np.load(All_Emoji_Vec_Nd_Path)

    print(All_Emoji_List[0])
    print(len(All_Emoji_Vec_Nd[0]))


