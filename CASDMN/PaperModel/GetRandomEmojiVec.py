# coding="utf-8"

import numpy as np
import tensorflow as tf

Parent_File_Path="/home/code_as_poetry/corpus_60000/"
All_Emoji_Path_List = Parent_File_Path+"All_Emoji_List.npy"

All_Emoji_Vec_Nd_Path = Parent_File_Path+"All_Emoji_Vec_Nd.npy"

EmojiDim = 300

if __name__=="__main__":
    print("GetRandomEmojiVec Main")

    All_Emoji_List = np.load(All_Emoji_Path_List)
    EmojiNum = len(All_Emoji_List)

    train_inputs = tf.placeholder(tf.int32, shape=[EmojiNum, EmojiDim])
    Emoji_Emddings = tf.Variable(tf.random_uniform([EmojiNum, EmojiDim], -1.0, 1.0))


    init = tf.global_variables_initializer()
    with tf.Session() as session:
        init.run()
        reult = session.run(Emoji_Emddings)
        # print("reult",type(reult),len(reult),reult.shape,reult)

    np.save(All_Emoji_Vec_Nd_Path,reult)


