# 文本查重算法
*本作业的github链接，<a href="https://github.com/LeoScott613/3121005269-SE/tree/master/duplicate_check">点击访问</a>*

## 个人软件过程PSP表记录
<table>
<tbody>
<tr>
<td width="192"><p><strong><strong>PSP2.1</strong></strong></p></td><td width="168">
<p><strong><strong>Personal Software Process Stages<strong></strong></p></td><td width="75">
<p><strong><strong>预估耗时（分钟）</strong></strong></p></td><td width="75"><p><strong><strong>实际耗时（分钟）</strong></strong></p></td></tr><tr><td width="192"><p>Planning</p>
</td>
<td width="168">
<p>计划</p>
</td>
<td width="75"><p>30</p></td><td width="75"><p>20</p>
</td></tr><tr><td width="192"><p>· Estimate</p></td>
<td width="168"><p>· 估计任务耗时</p></td><td width="75"><p>30</p></td><td width="75">
<p>20</p></td</tr><tr><td width="192"><p>Development</p></td><td width="168"><p>开发</p>
</td><td width="75"><p>210</p></td>
<td width="75"><p>290</p></td></tr>
<tr><td width="192"><p>· Analysis</p></td>
<td width="168"><p>· 需求分析 (包括学习新技术)</p></td><td width="75">
<p>50</p></td><td width="75"><p>30</p></td></tr>
<tr><td width="192"><p>· Design Spec</p></td><td width="168">
<p>· 生成设计文档</p>
</td>
<td width="75"><p>30</p></td><td width="75"><p>30</p>
</td></tr><tr><td width="192"><p>· Design Review</p>
</td><td width="168"><p>· 设计复审</p></td><td width="75"><p>20</p>
</td><td width="75"><p>30</p></td></tr><tr><td width="192">
<p>· Coding Standard</p>
</td>
<td width="168"><p>· 代码规范 (为目前的开发制定合适的规范)</p></td><td width="75"><p>10</p>
</td><td width="75"><p>10</p></td></tr>
<tr><td width="192"><p>· Design</p></td><td width="168">
<p>· 具体设计</p></td><td width="75"><p>20</p></td><td width="75"><p>25</p>
</td>
</tr>
<tr>
<td width="192">
<p>· Coding</p></td><td width="168"><p>· 具体编码</p>
</td><td width="75"><p>60</p></td><td width="75">
<p>80</p></td></tr><tr><td width="192">
<p>· Code Review</p></td><td width="168"><p>· 代码复审</p></td><td width="75"><p>10</p>
</td>
<td width="75">
<p>10</p>
</td>
</tr>
<tr>
<td width="192">
<p>· Test</p>
</td>
<td width="168">
<p>· 测试（自我测试，修改代码，提交修改）</p>
</td>
<td width="75">
<p>10</p>
</td><td width="75"><p>15</p></td></tr>
<tr><td width="192"><p>Reporting</p></td><td width="168">
<p>报告</p></td><td width="75"><p>60</p></td>
<td width="75"><p>60</p></td></tr><tr><td width="192">
<p>· Test Repor</p></td><td width="168"><p>· 测试报告</p></td><td width="75">
<p>20</p></td><td width="75"><p>20</p></td>
</tr><tr><td width="192"><p>· Size Measurement</p></td><td width="168"><p>· 计算工作量</p>
</td><td width="75"><p>20</p></td>
<td width="75"><p>20</p></td></tr><tr><td width="192"><p>· Postmortem &amp; Process Improvement Plan</p></td>
<td width="168"><p>· 事后总结, 并提出过程改进计划</p></td>
<td width="75"><p>20</p></td><td width="75"><p>20</p></td></tr><tr>
<td width="192"><p>&nbsp;</p></td><td width="168">
<p>·&nbsp;合计</p></td><td width="75"><p>300</p></td>
<td width="75"><p>370</p></td></tr></tbody></table>

## 计算模块接口的设计与实现过程
本程序的依赖要求
```python
sentence-transformers
paraphrase-multilingual-MiniLM-L12-v2
```

本程序使用sentence transformer提供的接口完成任务，引用的设计如下
```python
from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer
```

完成两句文本的相似度检查过程如下
```python
sentence1="当你竭尽所能却只能铩羽而归"
sentence2="当你竭尽所能却无法入睡"
st_model=SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
embedding1=st_model.encode(sentence1)
embedding2=st_model.encode(sentence2)
cosine_value=cos_sim(embedding1,embedding2)
print(cosine_value.item()*100,"%")
```
## 实际运行结果
![Alt text](run_result-1.jpg)