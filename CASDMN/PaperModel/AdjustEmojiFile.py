# coding="utf-8"

Parent_File_Path="/home/code_as_poetry/corpus_60000/"
Pos_Emoji_File_Path = Parent_File_Path+"Pos_Emoji.txt"
Neg_Emoji_File_Path = Parent_File_Path+"Neg_Emoji.txt"
Total_number = 60000

Adjust_Pos_Emoji_File_Path = Parent_File_Path+"Ad_Pos_Emoji.txt"
Adjust_Neg_Emoji_File_Path = Parent_File_Path+"Ad_Neg_Emoji.txt"

if __name__=="__main__":

    Pos_Emoji_File = open(Pos_Emoji_File_Path,"r")
    Adjust_Pos_Emoji_File = open(Adjust_Pos_Emoji_File_Path, "w")
    Pos_Emoji_Error_List=[]
    for i in range(Total_number):
        temp_str = Pos_Emoji_File.readline()
        if temp_str[1]!="[":
            Adjust_Pos_Emoji_File.write(" "+temp_str[temp_str.find("["):-1])
            if temp_str[temp_str.find("["):-1][-1]!="\n":
                Adjust_Pos_Emoji_File.write("\n")
            Pos_Emoji_Error_List.append(i)
        else:
            Adjust_Pos_Emoji_File.write(temp_str)
    print("Pos_Emoji_Error_List",len(Pos_Emoji_Error_List),Pos_Emoji_Error_List)


    Neg_Emoji_File = open(Neg_Emoji_File_Path, "r")
    Adjust_Neg_Emoji_File = open(Adjust_Neg_Emoji_File_Path, "w")
    Neg_Emoji_Error_List = []
    for i in range(Total_number):
        temp_str = Neg_Emoji_File.readline()
        if temp_str[1]!="[":
            Neg_Emoji_Error_List.append(i)
            Adjust_Neg_Emoji_File.write(temp_str[temp_str.find("["):-1])
            if temp_str[temp_str.find("["):-1][-1]!="\n":
                Adjust_Neg_Emoji_File.write("\n")
        else:
            Adjust_Neg_Emoji_File.write(temp_str)
    print("Neg_Emoji_Error_List", len(Neg_Emoji_Error_List), Neg_Emoji_Error_List)





