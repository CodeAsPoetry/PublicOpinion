# coding = "utf-8"

import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def plot_with_labels(low_dim_embs,labels,filename="/home/code_as_poetry/model_pic/tsne.png"):
    plt.figure(figsize=(18,18))
    for i,label in enumerate(labels):
        x,y = low_dim_embs[i,:]
        plt.scatter(x,y)
        plt.annotate(label,xy=(x,y),xytext=(5,2),textcoords='offset points',ha="right",va="bottom")
    plt.savefig(filename)


if __name__=="__main__":

    Emoji_model_path = "/home/code_as_poetry/Model_Emoji/"
    Emoji_Embedding_NPY_Path = Emoji_model_path + "emoji.npy"
    Emoji_Embedding = np.load(Emoji_Embedding_NPY_Path)
    print(Emoji_Embedding.shape,Emoji_Embedding)
    tsne = TSNE(perplexity=30,n_components=2,init='pca',n_iter=200)
    low_dim_embs = tsne.fit_transform(Emoji_Embedding)
    labels=[]
    for i in range(901):
        labels.append(i)
    print(low_dim_embs.shape,low_dim_embs)
    print(labels)
    plot_with_labels(low_dim_embs,labels)