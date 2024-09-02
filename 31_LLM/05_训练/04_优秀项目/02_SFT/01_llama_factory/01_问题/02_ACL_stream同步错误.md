# 参考Issue

- 910A推理qwen1.5chat模式可行，api模式报错aicpu exception #4666，https://github.com/hiyouga/LLaMA-Factory/issues/4666
- Ascend NPU训练成功但是推理报错 #3840，https://github.com/hiyouga/LLaMA-Factory/issues/3840

# 解决方法

- 在yaml配置文件中加入 do_sample: false
- 如果使用curl命令请求，需要在 curl 里面加 do_sample: false
- 如果使用openai 0.28.0版本，请求参数可能也需要加入 do_sample: false，因为该版本有这个参数 (实际未测试，用1.37.1版测试不需要加该参数，因为该版本没有这个参数)
