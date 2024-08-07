# 问题

使用多次调用同一个模型报错，首次调用generate并不会报错，后2次或者3次就会报错：

```text
libgomp: Thread creation failed: Resource temporarily unavailable

libgomp: 
libgomp: 
libgomp: Thread creation failed: Resource temporarily unavailableThread creation failed: Resource temporarily unavailableThread creation failed: Resource temporarily unavailable

libgomp: 
libgomp: Thread creation failed: Resource temporarily unavailableThread creation failed: Resource temporarily unavailable
libgomp: 

Thread creation failed: Resource temporarily unavailable

libgomp: Segmentation fault (core dumped)
```

代码：
```python
def worker_process():
    model= AutoModel(model="paraformer-zh",  vad_model="fsmn-vad",  punc_model="ct-punc", spk_model="cam++")
    wav_files = glob.glob('data/*/*/*.wav')
    for wav_file in wav_files:
        print('processing ',wav_file)
        output_path =f'{wav_file[:-4]}.json'
        start_time = time.time()
        ans = model.generate(input=wav_file,batch_size_s=300,hotword='', )
        os.system(f'rm "{wav_file}"')
        end_time = time.time()
        with open(output_path, 'w') as f:
            json.dump(ans, f, ensure_ascii=False)


if __name__ == '__main__':
    worker_process()

```

# 解决方案

 参考issue: libgomp: Thread creation failed: Resource temporarily unavailable #1798，https://github.com/modelscope/FunASR/issues/1798

该方案并不理想，每跑一个音频文件，模型就要重新加载一次，速度比较慢。

```python

def worker_process():
    wav_files = glob.glob('data/*/*/*.wav')
    for wav_file in wav_files:
        print('processing ',wav_file)
        output_path =f'{wav_file[:-4]}.json'
        start_time = time.time()
        model= AutoModel(model="paraformer-zh",  vad_model="fsmn-vad",  punc_model="ct-punc", spk_model="cam++")
        ans = model.generate(input=wav_file,batch_size_s=300,hotword='', )
        os.system(f'rm "{wav_file}"')
        end_time = time.time()
        with open(output_path, 'w') as f:
            json.dump(ans, f, ensure_ascii=False)


if __name__ == '__main__':
    worker_process()
```

# 参考

[1] libgomp: Thread creation failed: Resource temporarily unavailable #1798，https://github.com/modelscope/FunASR/issues/1798