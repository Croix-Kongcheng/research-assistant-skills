# scientific-visualization 效果示例

这两张图用技能中的视觉编码、等比例坐标、布局、色彩、注释与导出方法制作。所有输入均为原创的**数学示例或合成数据**，不能作为论文结论、无人机性能或配电网实验结果引用。

## 1. 无人机路线：长度与风险暴露

![无人机路线比较](output/01_uav_route_tradeoff.png)

同一起终点、障碍物和 50 m 网格，用 Dijkstra 分别求最短可行网格路线、风险加权网格路线。底色代表人为构造的无量纲风险场；灰色斜线区是禁止穿越的障碍。两条路线均采用八邻接、禁止斜向切角，并给障碍掩码增加半个网格对角线的保守边界。

风险暴露按路线上的梯形积分计算：`∑ Δs × (rᵢ+rᵢ₊₁)/2`，单位是 score-km。加权目标是 `长度 + 3 × 风险暴露`。这里的 3 是示例权重，量纲按给定归一化风险约定；它不代表真实事故概率或通用优化参数。路线长度是离散网格路径值，没有声称为连续空间的全局最优。

这张图展示等比例几何、连续变量色条、类别线色、直接注释和计算结果摘要。风险场完整数据见 [risk_grid.csv](output/risk_grid.csv)，路线坐标见 [最短路线](output/route_shortest.csv) 和 [风险加权路线](output/route_risk_weighted.csv)。

## 2. 配电恢复：恢复时间怎样影响缺供电量

![恢复时间和缺供电量](output/02_restoration_energy.png)

三个预设恢复时间表均在 8 h 时达到 100%，但恢复时序不同。假定总需求恒为 10 MW，以左端点数值保持到下一时刻（post-step），精确求每个区间的未恢复需求能量。左图阴影对应提前恢复时间表的未满足需求，右图汇总三种时间表的缺供电量。

这张图展示阶梯时间序列、共享单位、面积积分的物理解释以及与同一数据直接对应的条形摘要。数据见 [restoration_schedules.csv](output/restoration_schedules.csv)，全部公式参数和数值结果见 [parameters-and-results.json](output/parameters-and-results.json)。没有模拟拓扑、潮流、无人机调度、随机故障或优化算法，不能据此认定某项技术有效。

## 复现与导出

需要 Python、NumPy 和 Matplotlib；先检查现有环境。此目录不要求固定的操作系统、解释器位置或中文字体。

```bash
python make_figures.py
python make_figures.py --output-dir another-output
```

默认在本目录 `output/` 写入两张独立图，每张都包含 PNG、可编辑文字的 SVG 和嵌入字体的 PDF。脚本和参数可用于改图；运行时刻和实际库版本写入 JSON。原始书籍的图或代码没有复制到示例。

已在 Windows 的 Python 3.14、NumPy 2.4.6、Matplotlib 3.10.9 环境实际运行，并查看导出的 PNG 检查排版；这不代表所有目标阅读器、操作系统或打印设备均已验证。

## 许可

代码：[BSD-2-Clause](LICENSE-CODE)，版权 2026 Croix-Kongcheng and contributors。示例图、合成数据和本文：署名 **Croix-Kongcheng / research-assistant-skills**，采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，转载或修改时保留来源及改动说明。作者未声称原书作者认可这些示例。技能本身的书籍衍生知识文本另有 CC BY-NC-SA 4.0 许可，见 [技能许可](../../skills/scientific-visualization/LICENSE)。
