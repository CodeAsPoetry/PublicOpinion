# coding="utf-8"

import tensorflow as tf
import numpy as np
import word2vec
from tensorflow.contrib.rnn import GRUCell
from tensorflow.python.ops.rnn import bidirectional_dynamic_rnn as bi_rnn
from random import randint

batchSize=512
numClasses=2
maxSeqLength=100
wordDim = 300
hiddenSize = 150
DELAT=0.2

ParentFilePath="/home/code_as_poetry/SouGou/"
corpusWord2Vect=ParentFilePath+"corpusWord2Vec.bin"

Parent_File_Path="/home/code_as_poetry/corpus_60000/"

Pos_Txt_Index_List_Path=Parent_File_Path+"Pos_Txt_Index.npy"
Neg_Txt_Index_List_Path=Parent_File_Path+"Neg_Txt_Index.npy"

Total_Sample_Num = 120000

model_path = "/home/code_as_poetry/Model_ZH/"
log_dir = '/home/code_as_poetry/PaperPic'

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

def getTrainBatch(Train_Set,Pos_Txt_Index_List,Neg_Txt_Index_List):

    TrainBatchSampleIndex=[]

    TrainBatchWordIndex=[]

    TrainBatchWordVec=[]

    TrainBatchLabel=[]

    for i in range(batchSize):
        num = randint(0, 120000)
        while(num not in Train_Set):
            num = randint(0, 120000)
        TrainBatchSampleIndex.append(num)


    for i in range(batchSize):
        the_sample_index=[]
        if TrainBatchSampleIndex[i]<60000:
            the_sample_index_pri = Pos_Txt_Index_List[i]
            TrainBatchLabel.append([1,0])
        else:
            the_sample_index_pri = Neg_Txt_Index_List[i-60000]
            TrainBatchLabel.append([0,1])

        if len(the_sample_index_pri)>=maxSeqLength:
            for i in range(maxSeqLength):
                the_sample_index.append(the_sample_index_pri[i])
        else:
            while(len(the_sample_index_pri)<maxSeqLength):
                the_sample_index_pri.append(0)
            the_sample_index = the_sample_index_pri

        TrainBatchWordIndex.append(the_sample_index)

    for i in range(batchSize):
        the_sample_vec=[]
        the_sample_index = TrainBatchWordIndex[i]
        for j in range(maxSeqLength):
            the_sample_vec.append(model.vectors[the_sample_index[j]])
        TrainBatchWordVec.append(the_sample_vec)

    TrainBatchWordVec = np.array(TrainBatchWordVec)

    TrainBatchLabel = np.array(TrainBatchLabel)

    return TrainBatchSampleIndex,TrainBatchWordVec,TrainBatchLabel

def getValidBatch(Valid_Set,Pos_Txt_Index_List,Neg_Txt_Index_List):
    ValidBatchSampleIndex = []

    ValidBatchWordIndex = []

    ValidBatchWordVec = []

    ValidBatchLabel = []

    for i in range(batchSize):
        num = randint(0, 120000)
        while (num not in Valid_Set):
            num = randint(0, 120000)
        ValidBatchSampleIndex.append(num)

    for i in range(batchSize):
        the_sample_index = []
        if ValidBatchSampleIndex[i] < 60000:
            the_sample_index_pri = Pos_Txt_Index_List[i]
            ValidBatchLabel.append([1, 0])
        else:
            the_sample_index_pri = Neg_Txt_Index_List[i - 60000]
            ValidBatchLabel.append([0, 1])

        if len(the_sample_index_pri) >= maxSeqLength:
            for i in range(maxSeqLength):
                the_sample_index.append(the_sample_index_pri[i])
        else:
            while (len(the_sample_index_pri) < maxSeqLength):
                the_sample_index_pri.append(0)
            the_sample_index = the_sample_index_pri

        ValidBatchWordIndex.append(the_sample_index)

    for i in range(batchSize):
        the_sample_vec = []
        the_sample_index = ValidBatchWordIndex[i]
        for j in range(maxSeqLength):
            the_sample_vec.append(model.vectors[the_sample_index[j]])
        ValidBatchWordVec.append(the_sample_vec)

    ValidBatchWordVec = np.array(ValidBatchWordVec)

    ValidBatchLabel = np.array(ValidBatchLabel)

    return ValidBatchSampleIndex,ValidBatchWordVec, ValidBatchLabel

def getTestBatch(Test_Set,Pos_Txt_Index_List,Neg_Txt_Index_List):
    TestBatchSampleIndex = []

    TestBatchWordIndex = []

    TestBatchWordVec = []

    TestBatchLabel = []

    for i in range(batchSize):
        num = randint(0, 120000)
        while (num not in Test_Set):
            num = randint(0, 120000)
        TestBatchSampleIndex.append(num)

    for i in range(batchSize):
        the_sample_index = []
        if TestBatchSampleIndex[i] < 60000:
            the_sample_index_pri = Pos_Txt_Index_List[i]
            TestBatchLabel.append([1.0, 0.0])
        else:
            the_sample_index_pri = Neg_Txt_Index_List[i - 60000]
            TestBatchLabel.append([0.0, 1.0])

        if len(the_sample_index_pri) >= maxSeqLength:
            for i in range(maxSeqLength):
                the_sample_index.append(the_sample_index_pri[i])
        else:
            while (len(the_sample_index_pri) < maxSeqLength):
                the_sample_index_pri.append(0)
            the_sample_index = the_sample_index_pri

        TestBatchWordIndex.append(the_sample_index)

    for i in range(batchSize):
        the_sample_vec = []
        the_sample_index = TestBatchWordIndex[i]
        for j in range(maxSeqLength):
            the_sample_vec.append(model.vectors[the_sample_index[j]])
        TestBatchWordVec.append(the_sample_vec)

    TestBatchWordVec = np.array(TestBatchWordVec)

    TestBatchLabel = np.array(TestBatchLabel)

    return TestBatchSampleIndex,TestBatchWordVec, TestBatchLabel

if __name__=="__main__":
    print("CASDMN_Model")

    model = word2vec.load(corpusWord2Vect)
    Pos_Txt_Index_List = list(np.load(Pos_Txt_Index_List_Path))
    Neg_Txt_Index_List = list(np.load(Neg_Txt_Index_List_Path))


    Train_Set, Valid_Set,Test_Set = getSplitSets()


    tf.reset_default_graph()
    labels = tf.placeholder(tf.float32, [batchSize, numClasses])
    input_text = tf.placeholder(tf.float32, [batchSize, maxSeqLength,wordDim])
    input_emoji = tf.placeholder(tf.float32,[batchSize,wordDim])

    # (Bi-)RNN layer(-s)
    seq_len_ph = []
    for i in range(batchSize):
        seq_len_ph.append(maxSeqLength)
    rnn_outputs, _ = bi_rnn(GRUCell(hiddenSize), GRUCell(hiddenSize),
                            inputs=input_text, sequence_length=seq_len_ph, dtype=tf.float32)

    memory = tf.concat(rnn_outputs, 2)

    attention_input_1 = tf.reduce_mean(input_text, axis=1)



    def attention(memory, input):

        input = tf.reshape(input, [batchSize, 1, wordDim])

        inputs = input
        for i in range(memory.shape[1] - 1):
            inputs = tf.concat((inputs, input), 1)

        inputss = tf.concat((memory, inputs), 2)

        inputss = tf.transpose(inputss, [0, 2, 1])
        w = tf.Variable(tf.random_uniform([wordDim * 2, 1], -1.0, 1.0))
        b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

        alphas = tf.nn.softmax(tf.tanh(tf.tensordot(inputss, w, axes=([1], [0])) + b))

        attention_out = np.dot(memory, alphas)
        attention_out = tf.reduce_mean(attention_out, 1)
        input = tf.reshape(input, [batchSize, wordDim])
        attention_out = (1 - DELAT) * attention_out + DELAT * input
        return attention_out, alphas


    output_1, alphas_1 = attention(memory, attention_input_1)

    output_1 = tf.nn.dropout(output_1, 0.75)



    weight = tf.Variable(tf.truncated_normal([wordDim, numClasses]))
    bias = tf.Variable(tf.constant(0.1, shape=[numClasses]))
    prediction = tf.nn.softmax(tf.matmul(output_1, weight) + bias)


    # with tf.name_scope('cross_entropy'):
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=labels))
    # tf.summary.scalar('cross_entropy',loss)

    # with tf.name_scope('train'):
    optimizer = tf.train.AdamOptimizer(learning_rate=1e-3).minimize(loss)

    # with tf.name_scope('accuracy'):
    #     with tf.name_scope('correct_prediction'):
    correctPred = tf.equal(tf.argmax(prediction, 1), tf.argmax(labels, 1))
        # with tf.name_scope('accuracy'):
    accuracy = tf.reduce_mean(tf.cast(correctPred, tf.float32))
    # tf.summary.scalar('accuracy',accuracy)



    # with tf.Session() as sess:
    #     merged = tf.summary.merge_all()
    #     train_writer = tf.summary.FileWriter(log_dir + '/train', sess.graph)
    #     test_writer = tf.summary.FileWriter(log_dir+'/test')
    #     sess.run(tf.global_variables_initializer())
    #
    #     # saver = tf.train.Saver()
    #     print("Traing starting...")
    #
    #     for i in range(1000):
    #         _,TrainBatchWordVec, TrainBatchLabel = getTrainBatch(Train_Set, Pos_Txt_Index_List, Neg_Txt_Index_List)
    #
    #         summary,_ = sess.run([merged,optimizer], {input_text: TrainBatchWordVec, labels: TrainBatchLabel})
    #         train_writer.add_summary(summary,i)
    #
    #         acc = sess.run(accuracy, feed_dict={input_text: TrainBatchWordVec, labels: TrainBatchLabel})
    #         coat = sess.run(loss, feed_dict={input_text: TrainBatchWordVec, labels: TrainBatchLabel})
    #         if i % 10 == 0:
    #             print('Iter' + str(i * batchSize) + ", Minibatch Loss=" + \
    #                   '{:.6f}'.format(coat) + ", Training Accuracy=" + \
    #                   "{:.5f}".format(acc))
    #         if i % 10 == 0:
    #             _,ValidBatchWordVec, ValidBatchLabel = getValidBatch(Valid_Set, Pos_Txt_Index_List, Neg_Txt_Index_List)
    #             # save_path = saver.save(sess, model_path + "text_bi_att.ckpt", global_step=i)
    #             coat_valid = sess.run(loss, feed_dict={input_text: ValidBatchWordVec, labels: ValidBatchLabel})
    #             summary,acc_valid = sess.run([merged,accuracy], {input_text: ValidBatchWordVec, labels: ValidBatchLabel})
    #             print('Iter' + str(i * batchSize) + ", Minibatch Loss=" + \
    #                   '{:.6f}'.format(coat_valid) + ", Validing Accuracy=" + \
    #                   "{:.5f}".format(acc_valid))
    #             test_writer.add_summary(summary,i)
    #
    #     print("Training finished!")
    #
    #
    #     print("Testing start")
    #
    #     for i in range(10):
    #         _,TestBatchWordVec, TestBatchLabel = getTestBatch(Test_Set, Pos_Txt_Index_List, Neg_Txt_Index_List)
    #         acc = sess.run(accuracy, feed_dict={input_text: TestBatchWordVec, labels: TestBatchLabel})
    #         coat = sess.run(loss, feed_dict={input_text: TestBatchWordVec, labels: TestBatchLabel})
    #         print('Iter' + str(i * batchSize) + ", Minibatch Loss=" + \
    #               '{:.6f}'.format(coat) + ", Testing Accuracy=" + \
    #               "{:.5f}".format(acc))
    #
    #     print("Testing finished!")
    #
    #     train_writer.close()
    #     test_writer.close()


    with tf.Session() as sess:
        saver = tf.train.Saver()
        saver.restore(sess, "/home/code_as_poetry/Model_ZH/text_bi_att.ckpt-700")

        # print("Testing start")
        #
        # for i in range(10):
        #     _,TestBatchWordVec, TestBatchLabel = getTestBatch(model,Test_Set, Pos_Txt_Index_List, Neg_Txt_Index_List)
        #     acc = sess.run(accuracy, feed_dict={input_text: TestBatchWordVec, labels: TestBatchLabel})
        #     coat = sess.run(loss, feed_dict={input_text: TestBatchWordVec, labels: TestBatchLabel})
        #     sess.run(accuracy, {input_text: TestBatchWordVec, labels: TestBatchLabel})
        #     print('Iter' + str(i * batchSize) + ", Minibatch Loss=" + \
        #           '{:.6f}'.format(coat) + ", Testing Accuracy=" + \
        #           "{:.5f}".format(acc))
        #
        # print("Testing finished!")



        # Feature

        from sklearn.ensemble import GradientBoostingClassifier
        from sklearn import metrics
        from sklearn.metrics import confusion_matrix


        Emoji_model_path = "/home/code_as_poetry/Model_Emoji/"

        Emoji_Embedding_NPY_Path = Emoji_model_path + "emoji.npy"
        P_Path = Emoji_model_path + "P.npy"
        N_Path = Emoji_model_path + "N.npy"

        Emoji_Embedding = np.load(Emoji_Embedding_NPY_Path)
        P = np.load(P_Path)
        N = np.load(N_Path)

        # print("Emoji_Embedding",type(Emoji_Embedding),len(Emoji_Embedding),Emoji_Embedding)
        # print("P",type(P),len(P),P)
        # print("N",type(N),len(N),N)


        gbm0 = GradientBoostingClassifier(random_state=10)
        for i in range(2):
            emoji_feature = []
            TrainBatchSampleIndex, TrainBatchWordVec, TrainBatchLabel = getTrainBatch(Train_Set, Pos_Txt_Index_List,
                                                                                      Neg_Txt_Index_List)

            text_feature = sess.run(output_1, {input_text: TrainBatchWordVec, labels: TrainBatchLabel})
            # print(text_feature.shape, text_feature)
            for j in range(len(TrainBatchSampleIndex)):
                if TrainBatchSampleIndex[j] < 60000:
                    embed = tf.nn.embedding_lookup(Emoji_Embedding, P[j])
                    embed = tf.reduce_mean(embed, 0)
                    emoji_feature.append(sess.run(embed))
                else:
                    embed = tf.nn.embedding_lookup(Emoji_Embedding, N[j - 60000])
                    embed = tf.reduce_mean(embed, 0)
                    emoji_feature.append(sess.run(embed))

            emoji_feature = np.array(emoji_feature)
            # print("emoji_feature", emoji_feature.shape, emoji_feature)

            # final_feature = np.concatenate([text_feature, emoji_feature], axis=1)
            final_feature = text_feature
            print(i,"final_feature", final_feature.shape)

            y=[]
            for k in range(len(TrainBatchLabel)):
                if TrainBatchLabel[k][0]!=1.0:
                    y.append(0)
                else:
                    y.append(1)

            gbm0.fit(final_feature, y)

        for i in range(1):
            TestBatchSampleIndex, TestBatchWordVec, TestBatchLabel = getTestBatch(Test_Set, Pos_Txt_Index_List,
                                                                                      Neg_Txt_Index_List)
            emoji_feature = []

            text_feature = sess.run(output_1, {input_text: TestBatchWordVec, labels: TestBatchLabel})
            # print(text_feature.shape, text_feature)
            for j in range(len(TestBatchSampleIndex)):
                if TestBatchSampleIndex[j] < 60000:
                    embed = tf.nn.embedding_lookup(Emoji_Embedding, P[j])
                    embed = tf.reduce_mean(embed, 0)
                    emoji_feature.append(sess.run(embed))
                else:
                    embed = tf.nn.embedding_lookup(Emoji_Embedding, N[j - 60000])
                    embed = tf.reduce_mean(embed, 0)
                    emoji_feature.append(sess.run(embed))

            emoji_feature = np.array(emoji_feature)
            # print("emoji_feature", emoji_feature.shape, emoji_feature)

            # final_feature = np.concatenate([text_feature, emoji_feature], axis=1)
            final_feature = text_feature
            print("final_feature", final_feature.shape)

            y_pred = gbm0.predict(final_feature)

            y = []
            for k in range(len(TestBatchLabel)):
                if TestBatchLabel[k][0] != 1.0:
                    y.append(0)
                else:
                    y.append(1)

            print("Accuracy : %.4g" % metrics.accuracy_score(y, y_pred))
            C = confusion_matrix(y, y_pred)
            print(C)

            import matplotlib.pyplot as plt  # 导入作图库

            # plt.matshow(C, cmap=plt.cm.Blues)  # 画混淆矩阵图
            # plt.colorbar()  # 颜色标签
            #
            # for x in range(len(C)):  # 数据标签
            #     for y in range(len(C)):
            #         plt.annotate(C[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
            #
            # plt.ylabel('True label')  # 坐标轴标签
            # plt.xlabel('Predicted label')  # 坐标轴标签
            # plt.show()

            from sklearn.metrics import roc_curve  # 导入ROC曲线函数

            # 获取FPR,TPR的值
            fpr, tpr, thresholds = roc_curve(y, y_pred, pos_label=1)

            plt.plot(fpr, tpr, linewidth=2, label='ROC', color='blue')  # 作出ROC曲线
            plt.xlabel('False Positive Rate')  # 坐标轴标签
            plt.ylabel('True Positive Rate')  # 坐标轴标签
            plt.ylim(0, 1.05)  # 边界范围
            plt.xlim(0, 1.05)  # 边界范围
            plt.legend(loc=10)  # 图例
            plt.show()  # 显示作图结果

