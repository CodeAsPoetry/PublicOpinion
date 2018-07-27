# coding="utf-8"

import numpy as np

Parent_File_Path="/home/code_as_poetry/corpus_60000/"

Pos_Txt_Index_File_Path=Parent_File_Path+"Pos_Txt_Index.npy"
Neg_Txt_Index_File_Path=Parent_File_Path+"Neg_Txt_Index.npy"

Total_number=60000

if __name__=="__main__":

    Pos_Index_List = list(np.load(Pos_Txt_Index_File_Path))
    Neg_Index_List = list(np.load(Neg_Txt_Index_File_Path))

    Pos_Sample_Len_List=[]
    Neg_Sample_Len_List=[]

    for i in range(Total_number):
        Pos_Sample_Len_List.append(len(Pos_Index_List[i]))
        Neg_Sample_Len_List.append(len(Neg_Index_List[i]))

    print("Pos_Sample_Len_List",len(Pos_Sample_Len_List),max(Pos_Sample_Len_List),Pos_Sample_Len_List) # 106
    print("Neg_Sample_Len_List",len(Neg_Sample_Len_List),max(Neg_Sample_Len_List),Neg_Sample_Len_List) # 134

    # [0,10]       list_0
    # (10,20]      list_1
    # (20,30]      list_2
    # (30,40]      list_3
    # (40,50]      list_4
    # (50,60]      list_5
    # (60,70]      list_6
    # (70,80]      list_7
    # (80,90]      list_8
    # (90,100]     list_9
    # (100,110]    list_10
    # (110,120]    list_11
    # (120,130]    list_12
    # (130,140]    list_13

    list_0=0
    list_1=0
    list_2=0
    list_3=0
    list_4=0
    list_5=0
    list_6=0
    list_7=0
    list_8=0
    list_9=0
    list_10=0
    list_11=0
    list_12=0
    list_13=0

    for i in range(Total_number):
        the_sample_len = Pos_Sample_Len_List[i]
        if the_sample_len>=0 and the_sample_len<=10:
            list_0+=1
        if the_sample_len>10 and the_sample_len<=20:
            list_1+=1
        if the_sample_len>20 and the_sample_len<=30:
            list_2+=1
        if the_sample_len>30 and the_sample_len<=40:
            list_3+=1
        if the_sample_len>40 and the_sample_len<=50:
            list_4+=1
        if the_sample_len>50 and the_sample_len<=60:
            list_5+=1
        if the_sample_len>60 and the_sample_len<=70:
            list_6+=1
        if the_sample_len>70 and the_sample_len<=80:
            list_7+=1
        if the_sample_len>80 and the_sample_len<=90:
            list_8+=1
        if the_sample_len>90 and the_sample_len<=100:
            list_9+=1
        if the_sample_len>100 and the_sample_len<=110:
            list_10+=1
        if the_sample_len>110 and the_sample_len<=120:
            list_11+=1
        if the_sample_len>120 and the_sample_len<=130:
            list_12+=1
        if the_sample_len>130 and the_sample_len<=140:
            list_13+=1

        the_sample_len = Neg_Sample_Len_List[i]
        if the_sample_len >= 0 and the_sample_len <= 10:
            list_0 += 1
        if the_sample_len > 10 and the_sample_len <= 20:
            list_1 += 1
        if the_sample_len > 20 and the_sample_len <= 30:
            list_2 += 1
        if the_sample_len > 30 and the_sample_len <= 40:
            list_3 += 1
        if the_sample_len > 40 and the_sample_len <= 50:
            list_4 += 1
        if the_sample_len > 50 and the_sample_len <= 60:
            list_5 += 1
        if the_sample_len > 60 and the_sample_len <= 70:
            list_6 += 1
        if the_sample_len > 70 and the_sample_len <= 80:
            list_7 += 1
        if the_sample_len > 80 and the_sample_len <= 90:
            list_8 += 1
        if the_sample_len > 90 and the_sample_len <= 100:
            list_9 += 1
        if the_sample_len > 100 and the_sample_len <= 110:
            list_10 += 1
        if the_sample_len > 110 and the_sample_len <= 120:
            list_11 += 1
        if the_sample_len > 120 and the_sample_len <= 130:
            list_12 += 1
        if the_sample_len > 130 and the_sample_len <= 140:
            list_13 += 1

    print(list_0)
    print(list_1)
    print(list_2)
    print(list_3)
    print(list_4)
    print(list_5)
    print(list_6)
    print(list_7)
    print(list_8)
    print(list_9)
    print(list_10)
    print(list_11)
    print(list_12)
    print(list_13)

    total=list_0+list_1+list_2+list_3+list_4+list_5+list_6+list_7+list_8+list_9+list_10+list_11+list_12+list_13
    print(total)

    # 38155
    # 28547
    # 17758
    # 12030
    # 8646
    # 6313
    # 4537
    # 2793
    # 1050
    # 145
    # 21
    # 2
    # 2
    # 1
    # 120000


    # get 100, <100, index padding with 0
