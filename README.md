# OCR_CTPN-CRNN-CTCLoss

OCR used CTPN &amp; CRNN model and CTC Loss

## 描述

从自然场景图片中进行文字识别，包括2个步骤：

1、文字检测：解决的问题是哪里有文字，文字的范围有多少。

2、文字识别：对定位好的文字区域进行识别，主要解决的问题是每个文字是什么，将图像中的文字区域进转化为字符信息。

##文字检测CTPN

CTPN是在ECCV 2016提出的一种文字检测算法。CTPN结合CNN与LSTM深度网络，能有效的检测出复杂场景的横向分布的文字，效果如下图，是目前比较好的文字检测算法。

###介绍

CTPN是在ECCV2016提出的一种文字检测算法。CTPN结合CNN与LSTM深度网络，能有效的检测出复杂场景的横向分布的文字，效果如下图，是目前比较好的文字检测算法。

###创新点

1、将文本行拆分为slice进行检测，这样在检测过程中只需要对文本的高度进行先验性的设置anchor。
2、作者认为文本具有时序性，即和阅读习惯一直，从左到右。因此作者加入RNN获取这种语义性。
3、后处理算法：文本连接算法。

###注意点

1、由于加入LSTM，所以CTPN对水平文字检测效果超级好。

2、因为Anchor设定的原因，CTPN只能检测横向分布的文字，小幅改进加入水平Anchor即可检测竖直文字。但是由于框架限定，对不规则倾斜文字检测效果非常一般。

3、CTPN加入了双向LSTM学习文字的序列特征，有利于文字检测。但是引入LSTM后，在训练时很容易梯度爆炸，需要小心处理。

##文字识别CRNN

###介绍

CRNN全称为 Convolutional Recurrent Neural Network，主要用于端到端地对不定长的文本序列进行识别，不用先对单个文字进行切割，而是将文本识别转化为时序依赖的序列学习问题，就是基于图像的序列识别。

###网络结构

1、CNN（卷积层）：使用深度CNN，对输入图像提取特征，得到特征图。

2、RNN（循环层）：使用双向RNN（BLSTM）对特征序列进行预测，对序列中的每个特征向量进行学习，并输出预测标签（真实值）分布。

3、CTC loss（转录层）：使用CTC损失，把从循环层获取的一系列标签分布转换成最终的标签序列。

###CTC Loss

1、CRNN最难的地方，这一层为转录层，转录是将RNN对每个特征向量所做的预测转换成标签序列的过程。数学上，转录是根据每帧预测找到具有最高概率组合的标签序列。

2、端到端OCR识别的难点在于怎么处理不定长序列对齐的问题。OCR可建模为时序依赖的文本图像问题，然后使用CTC（Connectionist Temporal Classification, CTC）的损失函数来对CNN和RNN进行端到端的联合训练。

###注意点

1、预测过程中，先使用标准的CNN网络提取文本图像的特征，再利用BLSTM将特征向量进行融合以提取字符序列的上下文特征，然后得到每列特征的概率分布，最后通过转录层(CTC)进行预测得到文本序列。

2、利用BLSTM和CTC学习到文本图像中的上下文关系，从而有效提升文本识别准确率，使得模型更加鲁棒。

3、在训练阶段，CRNN将训练图像统一缩放为160×32（w×h）；在测试阶段，针对字符拉伸会导致识别率降低的问题，CRNN保持输入图像尺寸比例，但是图像高度还是必须统一为32个像素，卷积特征图的尺寸动态决定LSTM 的时序长度（时间步长）。
