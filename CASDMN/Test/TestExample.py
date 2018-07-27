# coding="utf-8"
# import word2vec
#
# teststr="aasssnnnnp"
# print(teststr[1:-1])
#
# ParentFilePath="/home/code_as_poetry/SouGou/"
# corpusWord2Vect=ParentFilePath+"corpusWord2Vec.bin"
#
# model = word2vec.load(corpusWord2Vect)
#
# help(model)
#
# print(model.get_vector("我"))
# print(model.vocab[50])
#
# print(model.get_vector(model.vocab[50]))
# print("--------------")
# print(model.vectors[50])

# Total_Sample_Num = 120000
#
# Train_Set=[]
# Valid_Set=[]
# Test_Set=[]
#
# for i in range(10000):
#     for j in range(12):
#         if j<10:
#             Train_Set.append(12*i+j)
#         else:
#             if j==10:
#                 Valid_Set.append(12*i+j)
#             if j==11:
#                 Test_Set.append(12*i+j)
#
#
#
# print("Train_Set",len(Train_Set),Train_Set)
# print("Valid_Set",len(Valid_Set),Valid_Set)
# print("Test_Set",len(Test_Set),Test_Set)

import tensorflow as tf
import word2vec
import numpy as np
import PaperModel.ASDMN_Text_Model as PMATM
from tensorflow.contrib.rnn import GRUCell
from tensorflow.python.ops.rnn import bidirectional_dynamic_rnn as bi_rnn

batchSize=512
numClasses=2
maxSeqLength=100
wordDim = 300
hiddenSize = 150
DELAT=0.2
model_path = "/home/code_as_poetry/Model_ZH/"
Parent_File_Path="/home/code_as_poetry/corpus_60000/"

Pos_Txt_Index_List_Path=Parent_File_Path+"Pos_Txt_Index.npy"
Neg_Txt_Index_List_Path=Parent_File_Path+"Neg_Txt_Index.npy"

ParentFilePath="/home/code_as_poetry/SouGou/"
corpusWord2Vect=ParentFilePath+"corpusWord2Vec.bin"

model = word2vec.load(corpusWord2Vect)
Train_Set, Valid_Set,Test_Set = PMATM.getSplitSets()
Pos_Txt_Index_List = list(np.load(Pos_Txt_Index_List_Path))
Neg_Txt_Index_List = list(np.load(Neg_Txt_Index_List_Path))

tf.reset_default_graph()
labels = tf.placeholder(tf.float32, [batchSize, numClasses])
input_text = tf.placeholder(tf.float32, [batchSize, maxSeqLength, wordDim])
input_emoji = tf.placeholder(tf.float32, [batchSize, wordDim])

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

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=labels))
optimizer = tf.train.AdamOptimizer(learning_rate=1e-3).minimize(loss)

correctPred = tf.equal(tf.argmax(prediction, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correctPred, tf.float32))

with tf.Session() as sess:
    saver = tf.train.Saver()
    saver.restore(sess, "/home/code_as_poetry/Model_ZH/text_bi_att.ckpt-700")



    print("Testing start")

    for i in range(10):
        TestBatchWordVec, TestBatchLabel = PMATM.getTestBatch(model,Test_Set, Pos_Txt_Index_List, Neg_Txt_Index_List)
        acc = sess.run(accuracy, feed_dict={input_text: TestBatchWordVec, labels: TestBatchLabel})
        coat = sess.run(loss, feed_dict={input_text: TestBatchWordVec, labels: TestBatchLabel})
        sess.run(accuracy, {input_text: TestBatchWordVec, labels: TestBatchLabel})
        print('Iter' + str(i * batchSize) + ", Minibatch Loss=" + \
              '{:.6f}'.format(coat) + ", Testing Accuracy=" + \
              "{:.5f}".format(acc))

    print("Testing finished!")


