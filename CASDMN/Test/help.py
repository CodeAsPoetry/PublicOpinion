import matplotlib.pyplot as plt  # 导入作图库
import numpy as np
C=[[100,2],[8,100]]
C=np.array(C)
plt.matshow(C, cmap=plt.cm.Blues)  # 画混淆矩阵图
plt.colorbar()  # 颜色标签

for x in range(len(C)):  # 数据标签
    for y in range(len(C)):
        plt.annotate(C[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')

plt.ylabel('True label')  # 坐标轴标签
plt.xlabel('Predicted label')  # 坐标轴标签
plt.show()

