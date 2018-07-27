# coding = "utf-8"

import word2vec

ParentFilePath="/home/code_as_poetry/SouGou/"
ProFilePath=ParentFilePath+"split_corpus.txt"
corpusWord2Vect=ParentFilePath+"corpusWord2Vec.bin"

if __name__=="__main__":
    print("GetWord2VecZH.py")

    # Run one time
    # word2vec.word2vec(ProFilePath,corpusWord2Vect,size=300,verbose=True)