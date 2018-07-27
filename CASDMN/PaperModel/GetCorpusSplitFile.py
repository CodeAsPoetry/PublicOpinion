# coding="utf-8"

import jieba

Parent_File_Path="/home/code_as_poetry/corpus_60000/"
Pos_Txt_File_Path=Parent_File_Path+"Ad_Pos_Txt.txt"
Neg_Txt_File_Path=Parent_File_Path+"Ad_Neg_Txt.txt"
Total_number=60000

Split_Pos_Txt_File_Path=Parent_File_Path+"Ad_Split_Pos_Txt.txt"
Split_Neg_Txt_File_Path=Parent_File_Path+"Ad_Split_Neg_Txt.txt"


if __name__=="__main__":
    print()

    Pos_Txt_File = open(Pos_Txt_File_Path,"r")
    Neg_Txt_File = open(Neg_Txt_File_Path,"r")

    Pos_List = []
    Neg_List = []
    for i in range(Total_number):
        Pos_List.append(Pos_Txt_File.readline())
        Neg_List.append(Neg_Txt_File.readline())

    print(Pos_List[59999])
    print(Neg_List[59999])

    Split_Pos_Txt_File = open(Split_Pos_Txt_File_Path,"w")
    Split_Neg_Txt_File= open(Split_Neg_Txt_File_Path,"w")

    # Run one time

    # for i in range(Total_number):
    #     print(' '.join(jieba.cut(Pos_List[i],cut_all=False)))
    #     Split_Pos_Txt_File.write(' '.join(jieba.cut(Pos_List[i],cut_all=False)))
    #
    #     print(' '.join(jieba.cut(Neg_List[i], cut_all=False)))
    #     Split_Neg_Txt_File.write(' '.join(jieba.cut(Neg_List[i], cut_all=False)))