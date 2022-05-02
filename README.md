# PublicOpinion
## 0. 引言

此项目包括與情分析系统，包括爬虫、数据清洗、文本摘要、主题分类、情感倾向性识别以及分析结果数据可视化。该项目是在校时导师建议的一个边缘研究方向，开题时间 2017 上半年。导师研究的主力方向是网络空间安全，因此在社会工程学上，以当时大火的 AI 领域 NLP (自然语言处理) 为切入口，进行舆情舆论的情感倾向性研究。当时 NLP 的领域还是战国时代，self-attention 还在萌芽，transformers 还在酝酿，现在占统治地位的 BERT 和预训练机制还没有问世。战火纷飞的前 BERT 时代，百家争鸣，基于加性和乘性的传统 Attention 配合着 LSTM、GRU 等，花活儿辈出，创新方向是模型的魔改以及结合数据和场景的词嵌入。因此当时的建模方法相对今日早已落后。但是舆情分析的应用场景一直存在并且越来越需要，尤其是后疫情时代。所幸毕业之后一直从事 NLP 算法的工作，在项目的重构、建模的创新、以及整个工程应用链路的打通，也有很大成长，希望让这个项目完善起来，能帮助到社区，帮助到各位。

## 1. 项目背景

相信上至政府、企业，下到团体、个人，经历过新冠疫情，都深深意识到，网络舆情的重要程度。特殊时刻甚至能够左右时局、事态的发展。与此同时，后 BERT 时代，自然语言处理技术已经得到快速并且深入的发展。希望能有一个便捷的工具，可以更高效方便地收集网络舆情，通过情绪极性自动识别，分析舆论风向；有必要的话，自动抽取舆情中关注的重要信息，为使用者提供更精准及时的决策依据。技术工具本无好坏，重在使用者的初心。希望世界和平稳定，没有战争、没有疫情、人人安居乐业，技术造福人类。

## 2. 项目调研

### 2.1 舆情数据获取

#### 2.1.1 舆情的定义

所谓网络，互联网等，本质上就是一个信息载体，整个社会的信息在其中产生、演变、交互、消失。这些海量信息冗余繁杂、真假难辨，那么什么样的信息才算舆情。将复杂问题极致简化，时钟拨回人类的原始社会时期，那时信息极致简单明了，除了渔猎、迁徙、繁衍无他。舆情便是：原始人讨论去哪里渔猎、讨论迁徙到哪里、讨论如何繁衍。从中可以看到，舆情便是群体中大多数人所关注的、具有价值的信息。大多数人关注、具有价值，这两点缺一不可。而在现在的分工极为细致的信息社会，多少人参与讨论以及有无价值是相对于舆情获取者及关注问题而言的，因此，这两个标准要在最开始时明确。

#### 2.1.2 网络舆情的来源

云计算、云存储、大算力的进步，为信息能够以指数爆炸式地增长提供技术保障；以前的论坛、贴吧、社区，现在的微博、知乎、微信、抖音等，大量鼓励用户生成内容(UGC)的诞生，让信息能够被大多数人创作、演变、交互，同时也让信息变得更分散、更低质；大火的要上链的 web 3.0、区块链让信息变得更加隐私匿名。同时，网络信息形式越来越多样化，文本、表情包、音频、视频等，也为舆情获取提高门槛。此外，商业化的大规模的水军行为也让互联网内容环境越来越复杂。因此随着信息越来越浩瀚、越来越低质、越来越分散、越来越私密，收集大多数人关注的、有价值的网络信息越来越难。

以目前的状态，从技术视角来看，网络舆情的获取，移动端APP占绝大多数，此外，兼顾传统媒体，一些 Web 站点等也需纳入考虑。具体来说，公共事件的话，微博，微信公众号、视频号，抖音号，知乎这些必然是要有的；消费商品评价的话，各大电商平台，如淘宝、天猫、京东、当当、拼多多、自营商城网站等(比如对于电子产品，中关村在线)是肯定要有的；游戏、体育、图书、影视剧、艺术展的话，豆瓣、虎扑等是要有的。

#### 2.1.3 网络舆情的获取

目前获取网络舆情的主要技术方法，还是通过爬虫获取，包括网站爬虫、APP爬虫。最近各种隐私数据保护政策的落地，以及公司对数据资产的重视，爬虫和反爬技术愈演愈烈，小爬怡情，大爬伤身，强爬灰飞烟灭。

* Web 爬虫
* APP 爬虫

### 2.2 舆情数据分析

#### 2.2.1 网络舆情的分类

* 舆情主题分类，获取目标受众关注的热点方向、热点领域，常用于造势，预测热点，并利用热点宣发，或者打造爆款
* 受众偏好分类，获取目标受众的审美、口味、偏好的趋势，常用于顺势时尚，调整宣发策略
* 舆情受众画像，根据受众的画像，对舆情分门别类，出于不同目的，推送给受众，吸睛引流

#### 2.2.2 网络舆情的情感极性

* 篇章/段落粒度的情感极性
* 句子粒度的情感极性
* 细粒度目标的情感极性(aspect-level)

#### 2.2.3 网络舆情的信息

* 获取网络舆情自身的关键信息，如主体、关系、客体；时间、地点等
* 获取参与网络舆情目标受众的态度、观点、看法等
* 获取网络舆情的时间线、主题等，预测舆情以及受众态度的走势

## 3. 建模思路

### 3.1 舆情主题识别及分类——分类

* 思路：主题分类，典型的自然语言理解 (NLU) 研究方向之一，对于有较强的业务意图的场景，主题类别确定，有监督的分类都可尝试；主题类别不确定，垂直域可以尝试支持类别扩充的有监督分类，开放域建议尝试无监督分类；对于现在舆情信息的形式多样，文本，图片，表情包，音频、视频等，多模态必是未来趋势；对于数据获取以及存储的效率来看，首选文本，如果文本形式即可满足场景需求，则大道至简。
* 参考：大量的论文、模型、数据、竞赛资源
* 模型：规则策略、特征工程+传统机器学习、深度学习

### 3.2 情感极性识别——分类

* 思路：情感极性分类，典型的自然语言理解 (NLU) 研究方向之一，根据业务场景的分析粒度，选择对应的研究对象
* 参考：大量的论文、模型、数据、竞赛资源
* 模型：规则策略、特征工程+传统机器学习、深度学习

### 3.3 舆情摘要生成——短文本生成

* 思路：短文本生成，典型的自然语言生成 (NLG) 研究方向之一，生成较为成熟，条件生成、可控性都有一定保障
* 参考：大量的论文、模型、数据、竞赛资源
* 模型：规则模板、话术底表、特征工程+传统机器学习、深度学习

### 3.4 舆情关键信息抽取——信息抽取

* 思路：信息抽取，pipeline形式，还是end-to-end联合抽取，重点 NLP 领域研究方向，成熟稳定，各大竞赛的常见场景
* 参考：大量的论文、模型、数据、竞赛资源
* 模型：规则模板、特征工程+传统机器学习、深度学习(有无 Schema 约束)

## 4. 项目过程

### 4.1 网络舆情爬取

### 4.2 舆情数据清洗及统计分析

### 4.3 Baseline 模型

#### 4.3.1 主题识别——文本分类

#### 4.3.2 舆情情感极性识别——文本分类

#### 4.3.3 舆情摘要生成——文本生成

#### 4.3.4 舆情信息抽取——信息抽取

### 4.4 BadCase分析及模型优化

### 4.5 舆情数据可视化

### 4.6 建立服务部署

### 4.7 建立工程应用平台

## 5. 结项免责&使用说明





