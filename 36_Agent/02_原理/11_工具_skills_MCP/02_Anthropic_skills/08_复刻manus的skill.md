https://github.com/OthmanAdi/planning-with-files.git

1. task_plan.md（指挥塔 寄存器）
这是整个架构的核心。它不存储具体知识，只存储元数据。

作用：定义目标、拆解阶段、追踪进度、记录错误。

关键机制：它是Agent的“罗盘”。无论任务进行到第几步，Agent必须在每次行动前读取此文件。

2. notes.md（知识库 堆内存）
作用：存储调研笔记、网页摘要、中间代码。

关键机制：“Store, Don't Stuff”。当Agent搜索到大量资料时，禁止直接输出到对话框，必须写入此文件。这保持了对话上下文的清爽。

3. [deliverable].md（产出物 IO缓冲区）
作用：最终的交付结果（如 game.py 或 report.md）。

关键机制：将“思考过程”与“最终结果”物理隔离。