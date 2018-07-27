# coding="utf-8"


Parent_File_Path="/home/code_as_poetry/corpus_60000/"
Pos_File_Path=Parent_File_Path+"pos60000.txt"
Neg_File_Path=Parent_File_Path+"neg60000.txt"
Total_Line_Number=60000

ProcessedTxt_Pos_File_Path=Parent_File_Path+"Pos_Txt_Emoji.txt"
ProcessedTxt_Neg_File_Path=Parent_File_Path+"Neg_Txt_Emoji.txt"

def find_atsb(strline):
    op_index=[]
    for i in range(len(strline)):
        for j in range(i,len(strline)):
            if (strline[i] == "@"):
                if(strline[j]==' ' or strline[j]=='：' or strline[j]==":" or strline[j]=="\n"):
                    op_index.append([i,j])
                    break
                else:
                    continue
            else:
                continue
    return op_index

def getText_emoji(strline):

    op_index = find_atsb(strline)
    newstr = ""
    for i in range(len(strline)):
        skip_index = []
        for j in range(len(op_index)):
            if i>=op_index[j][0] and i<=op_index[j][1]:
                skip_index.append(i)

        if i not in skip_index:
            newstr += strline[i]

    return newstr

def GetChineseWord_Emoji(ProcessedTxt_File_Path,templist):

    Txt_Emoji_File = open(ProcessedTxt_File_Path, "w")
    for i in range(len(templist)):
        newstr=getText_emoji(templist[i])
        print(newstr)
        if newstr!="" and newstr[-1]=="\n":
            Txt_Emoji_File.write(newstr)
        else:
            Txt_Emoji_File.write(newstr+"\n")
    Txt_Emoji_File.close()

if __name__=="__main__":
    print("ProcessFile_Main")
    Pos_File = open(Pos_File_Path,"r")
    Neg_File = open(Neg_File_Path,"r")

    Pos_List=[]
    Neg_List=[]
    for i in range(Total_Line_Number):
        Pos_List.append(Pos_File.readline())
        Neg_List.append(Neg_File.readline())

    print(len(Pos_List))
    print(len(Neg_List))
    # Run one time
    # GetChineseWord_Emoji(ProcessedTxt_Pos_File_Path,Pos_List)
    # GetChineseWord_Emoji(ProcessedTxt_Neg_File_Path, Neg_List)

