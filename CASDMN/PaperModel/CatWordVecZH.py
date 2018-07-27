# coding="utf-8"

import word2vec

ParentFilePath="/home/code_as_poetry/SouGou/"
corpusWord2Vect=ParentFilePath+"corpusWord2Vec.bin"

if __name__=="__main__":
    model = word2vec.load(corpusWord2Vect)

    indexes = model.cosine(u'清华大学')
    print(u"与‘清华大学’相近的词：")
    for index in indexes[0]:
        print (model.vocab[index])