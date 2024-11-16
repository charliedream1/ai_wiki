启动训练脚本
===================

用户在安装了InternEvo之后，需要自行编写训练启动脚本，请参考： `train.py <https://github.com/InternLM/InternEvo/blob/develop/train.py>`_

脚本中的流程可以分为三步：参数解析、初始化、启动训练。其中参数解析和初始化过程的具体原理参见： `训练初始化 <https://internevo.readthedocs.io/zh-cn/latest/initialize.html>`_

配置参数解析
------------------------
.. code-block:: python

    args = parse_args()

调用 ``parse_args`` 函数，解析在启动训练传入的配置文件中设置的参数。详见： `命令行参数解析 <https://internevo.readthedocs.io/zh-cn/latest/initialize.html#internlm-args>`_

初始化过程
------------------------
- 初始化分布式训练环境
.. code-block:: python

    initialize_distributed_env(config=args.config, launcher=args.launcher, master_port=args.port, seed=args.seed)

调用 ``initialize_distributed_env`` 函数，支持通过 slurm 或 torch 方式启动训练脚本，并传入配置文件、端口号、进程随机种子等信息。函数详细说明如下：

.. autofunction:: internlm.initialize.initialize_distributed_env

- 初始化模型
.. code-block:: python

    model = initialize_model()

详细介绍请参考： `模型初始化 <https://internevo.readthedocs.io/zh-cn/latest/initialize.html#internlm-model-init>`_

- 初始化训练数据加载器
.. code-block:: python

    train_dl, dataset_types = build_train_loader_with_data_type()

详细介绍请参考： `数据加载器初始化 <https://internevo.readthedocs.io/zh-cn/latest/initialize.html#internlm-dl-init>`_

- 初始化验证数据加载器
.. code-block:: python

    val_dls = build_valid_loader_with_data_type()

初始化验证数据加载器，加载过程与训练数据加载类似，通过配置文件中的 ``VALID_FOLDER `` 字段设置验证数据集路径。

- 初始化Trainer
.. code-block:: python

    trainer = TrainerBuilder(model, train_dl, val_dls, **kwargs)

这里 ``TrainerBuilder`` 接口继承自 ``Trainer`` 类，InternEvo 的训练 API 由 ``internlm.core.trainer.Trainer`` 管理。在定义了训练引擎和调度器之后，我们可以调用 Trainer API 来执行模型训练、评估、梯度清零和参数更新等。

有关详细用法，请参阅 Trainer API 文档和示例。

.. autoclass:: internlm.core.trainer.Trainer
    :members:

启动训练过程
------------------
.. code-block:: python

    trainer.fit()

首先，通过 ``self.train()`` 方法，将模型设置为training状态。

在每一步训练的过程中，通过 ``load_new_batch`` 加载数据集。
然后通过 ``execute_schedule`` 调度器启动训练，调用 ``forward_backward_step`` 开始forward及backward训练过程。
之后，通过 ``self.step()`` 更新参数，并返回梯度值。
如果达到了需要验证的step数，则通过 ``evaluate_on_val_dls`` 对模型训练结果进行评估。
最后，如果开启了保存ckpt功能，通过 ``try_save_checkpoint`` 函数保留训练中间状态以及最终训练结果。
