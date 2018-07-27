# coding="utf-8"

import numpy as np
import math
import tensorflow as tf
from random import randint

Parent_File_Path="/home/code_as_poetry/corpus_60000/"

All_Emoji_List_Path = Parent_File_Path+"All_Emoji_List.npy"

Pos_Emoji_Index_List_Path = Parent_File_Path+"Pos_Emoji_Index.npy"
Neg_Emoji_Index_List_Path = Parent_File_Path+"Neg_Emoji_Index.npy"

# model_path = "/home/code_as_poetry/Model_Emoji/"
#
# Emoji_Embedding_NPY_Path = model_path+"emoji.npy"
#
# P_Path = model_path+"P.npy"
# N_Path = model_path+"N.npy"


def getEmojiIndexList(Pos_Emoji_Index_List,Neg_Emoji_Index_List):
    P=[]
    N=[]
    for i in range(60000):
        temp_list = []
        if len(Pos_Emoji_Index_List[i])>=10:
            for j in range(10):
                temp_list.append(Pos_Emoji_Index_List[i][j])
            P.append(temp_list)
        else:
            for j in range(len(Pos_Emoji_Index_List[i])):
                temp_list.append(Pos_Emoji_Index_List[i][j])
            for j in range(len(Pos_Emoji_Index_List[i]),10):
                temp_list.append(900)
            P.append(temp_list)

    for i in range(60000):
        temp_list = []
        if len(Neg_Emoji_Index_List[i])>=10:
            for j in range(10):
                temp_list.append(Neg_Emoji_Index_List[i][j])
            N.append(temp_list)
        else:
            for j in range(len(Neg_Emoji_Index_List[i])):
                temp_list.append(Neg_Emoji_Index_List[i][j])
            for j in range(len(Neg_Emoji_Index_List[i]),10):
                temp_list.append(900)
            N.append(temp_list)

    return P,N

def getSplitSets():
    Train_Set=[]
    Valid_Set=[]
    Test_Set=[]
    for i in range(10000):
        for j in range(12):
            if j < 10:
                Train_Set.append(12 * i + j)
            else:
                if j == 10:
                    Valid_Set.append(12 * i + j)
                if j == 11:
                    Test_Set.append(12 * i + j)

    return Train_Set,Valid_Set,Test_Set

def getTrainBatch(Train_Set,P,N):

    TrainBatchSampleIndex=[]

    TrainBatchInputList=[]
    TrainBatchLabelList=[]

    for i in range(BatchSize):
        num = randint(0, 120000)
        while(num not in Train_Set):
            num = randint(0, 120000)
        TrainBatchSampleIndex.append(num)

    for i in range(len(TrainBatchSampleIndex)):
        if TrainBatchSampleIndex[i]<60000:
            TrainBatchInputList.append(P[i])
            TrainBatchLabelList.append([1.0,0.0])
        else:
            TrainBatchInputList.append(N[i-60000])
            TrainBatchLabelList.append([0.0,1.0])

    TrainBatchInputList = np.array(TrainBatchInputList)
    TrainBatchLabelList = np.array(TrainBatchLabelList)


    return TrainBatchInputList,TrainBatchLabelList

def getValidBatch(Valid_Set,P,N):
    ValidBatchSampleIndex = []

    ValidBatchInputList = []
    ValidBatchLabelList = []

    for i in range(BatchSize):
        num = randint(0, 120000)
        while (num not in Valid_Set):
            num = randint(0, 120000)
        ValidBatchSampleIndex.append(num)

    for i in range(len(ValidBatchSampleIndex)):
        if ValidBatchSampleIndex[i] < 60000:
            ValidBatchInputList.append(P[i])
            ValidBatchLabelList.append([1.0, 0.0])
        else:
            ValidBatchInputList.append(N[i - 60000])
            ValidBatchLabelList.append([0.0, 1.0])

    ValidBatchInputList = np.array(ValidBatchInputList)
    ValidBatchLabelList = np.array(ValidBatchLabelList)



    return ValidBatchInputList, ValidBatchLabelList

def getTestBatch(Test_Set,P,N):
    TestBatchSampleIndex = []

    TestBatchInputList = []
    TestBatchLabelList = []

    for i in range(BatchSize):
        num = randint(0, 120000)
        while (num not in Test_Set):
            num = randint(0, 120000)
        TestBatchSampleIndex.append(num)

    for i in range(len(TestBatchSampleIndex)):
        if TestBatchSampleIndex[i] < 60000:
            TestBatchInputList.append(P[i])
            TestBatchLabelList.append([1.0, 0.0])
        else:
            TestBatchInputList.append(N[i - 60000])
            TestBatchLabelList.append([0.0, 1.0])

    TestBatchInputList = np.array(TestBatchInputList)
    TestBatchLabelList = np.array(TestBatchLabelList)


    return TestBatchInputList, TestBatchLabelList

if __name__=="__main__":
    print("Emoji_Model Main")



    All_Emoji_List = list(np.load(All_Emoji_List_Path))
    Pos_Emoji_Index_List = list(np.load(Pos_Emoji_Index_List_Path))
    Neg_Emoji_Index_List = list(np.load(Neg_Emoji_Index_List_Path))

    Emoji_Num = len(All_Emoji_List) + 1  # index=900 padding
    Embedding_Size = 10
    BatchSize = 512
    NumClass = 2
    MaxSeq = 10

    Train_Set, Valid_Set, Test_Set = getSplitSets()
    P,N = getEmojiIndexList(Pos_Emoji_Index_List,Neg_Emoji_Index_List)

    # np.save(P_Path,P)
    # np.save(N_Path,N)

    TrainBatchInputList, TrainBatchLabelList = getTrainBatch(Train_Set,P,N)



    # (Max_Length:Pos=40,Neg=65)    (<10,N:59063;P:59428)


    tf.reset_default_graph()
    train_inputs = tf.placeholder(tf.int32,[BatchSize,MaxSeq])
    train_labels = tf.placeholder(tf.float32,[BatchSize,NumClass])


    embeddings = tf.Variable(tf.random_uniform([Emoji_Num,Embedding_Size],-1.0,1.0))

    embed = tf.nn.embedding_lookup(embeddings,train_inputs)

    input_data = tf.reduce_mean(embed,1)

    forw_weight = tf.Variable(tf.truncated_normal([Embedding_Size,NumClass],stddev=1.0/math.sqrt(Embedding_Size)))
    forw_biases = tf.Variable(tf.zeros([NumClass]))

    prediction = tf.nn.softmax(tf.matmul(input_data, forw_weight) + forw_biases)

    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=train_labels))
    optimizer = tf.train.AdamOptimizer(learning_rate=1e-3).minimize(loss)

    correctPred = tf.equal(tf.argmax(prediction, 1), tf.argmax(train_labels, 1))
    accuracy = tf.reduce_mean(tf.cast(correctPred, tf.float32))


    emdedding_writer = tf.summary.FileWriter(log_dir+'/embedding')

    with tf.Session() as sess:
        # saver = tf.train.Saver()
        sess.run(tf.global_variables_initializer())
        print("Traing starting...")

        for i in range(1000):
            TrainBatchInputList, TrainBatchLabelList = getTrainBatch(Train_Set, P, N)

            sess.run(optimizer, {train_inputs: TrainBatchInputList, train_labels: TrainBatchLabelList})

            acc = sess.run(accuracy, feed_dict={train_inputs: TrainBatchInputList, train_labels: TrainBatchLabelList})
            coat = sess.run(loss, feed_dict={train_inputs: TrainBatchInputList, train_labels: TrainBatchLabelList})
            if i % 10 == 0:
                print('Iter' + str(i * BatchSize) + ", Minibatch Loss=" + \
                      '{:.6f}'.format(coat) + ", Training Accuracy=" + \
                      "{:.5f}".format(acc))
            if i % 100 == 0:
                ValidBatchInputList, ValidBatchLabelList = getValidBatch(Valid_Set, P, N)
                # save_path = saver.save(sess, model_path + "emoji_embedding.ckpt", global_step=i)
                sess.run(accuracy, {train_inputs: ValidBatchInputList, train_labels: ValidBatchLabelList})
                print('Iter' + str(i * BatchSize) + ", Minibatch Loss=" + \
                      '{:.6f}'.format(coat) + ", Validing Accuracy=" + \
                      "{:.5f}".format(acc))

                # if i==700:
                #     np.save(Emoji_Embedding_NPY_Path,sess.run(embeddings, {train_inputs: ValidBatchInputList, train_labels: ValidBatchLabelList}))


        print("Training finished!")


        print("Testing start")

        for i in range(10):
            TestBatchInputList, TestBatchLabelList = getTestBatch(Test_Set, P, N)
            acc = sess.run(accuracy, feed_dict={train_inputs: TestBatchInputList, train_labels: TestBatchLabelList})
            coat = sess.run(loss, feed_dict={train_inputs: TestBatchInputList, train_labels: TestBatchLabelList})
            sess.run(accuracy, {train_inputs: TestBatchInputList, train_labels: TestBatchLabelList})
            print('Iter' + str(i * BatchSize) + ", Minibatch Loss=" + \
                  '{:.6f}'.format(coat) + ", Testing Accuracy=" + \
                  "{:.5f}".format(acc))

        print("Testing finished!")


    # with tf.Session() as sess:
    #     saver = tf.train.Saver()
    #     saver.restore(sess, model_path+"emoji_embedding.ckpt-700")
    #
    #     print("Testing start")
    #
    #     for i in range(10):
    #         TestBatchInputList, TestBatchLabelList = getTestBatch(Test_Set, P, N)
    #         acc = sess.run(accuracy, feed_dict={train_inputs: TestBatchInputList, train_labels: TestBatchLabelList})
    #         coat = sess.run(loss, feed_dict={train_inputs: TestBatchInputList, train_labels: TestBatchLabelList})
    #         sess.run(accuracy, {train_inputs: TestBatchInputList, train_labels: TestBatchLabelList})
    #         print('Iter' + str(i * BatchSize) + ", Minibatch Loss=" + \
    #               '{:.6f}'.format(coat) + ", Testing Accuracy=" + \
    #               "{:.5f}".format(acc))
    #
    #     print("Testing finished!")
