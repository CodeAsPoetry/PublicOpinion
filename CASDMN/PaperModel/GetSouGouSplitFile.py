# coding="utf-8"

import jieba

ParentFilePath="/home/code_as_poetry/SouGou/"
PriFilePath=ParentFilePath+"corpus.txt"
ProFilePath=ParentFilePath+"split_corpus.txt"

if __name__=="__main__":
    print("GetSouGouSplitFile Main")

    # Run one time

    # PriList=[]
    # with open(PriFilePath) as PriFile:
    #     for line in PriFile:
    #         PriList.append(line)
    #
    # ProList=[]
    # for i in range(len(PriList)):
    #     ProList.append(' '.join(jieba.cut(PriList[i][9:-11],cut_all=False)))
    #     if i%100 ==0:
    #         print(ProList[i])
    #
    # with open(ProFilePath, 'w') as ProFile:
    #     for i in range(len(PriList)):
    #         ProFile.write(ProList[i])
    #         ProFile.write("\n")
    #         if i%100 ==0:
    #             print(ProList[i])

