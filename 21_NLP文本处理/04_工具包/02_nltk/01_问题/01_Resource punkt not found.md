# 问题

错误描述

```text
LookupError: 
**********************************************************************
  Resource punkt not found.
  Please use the NLTK Downloader to obtain the resource:

  >>> import nltk
  >>> nltk.download('punkt')
  
  For more information see: https://www.nltk.org/data.html

  Attempted to load tokenizers/punkt/english.pickle

  Searched in:
    - 'C:/msys/1.0/home/nltk_data'
    - 'C:\\Users\\16662\\AppData\\Local\\Programs\\Python\\Python37\\nltk_data'
    - 'C:\\Users\\16662\\AppData\\Local\\Programs\\Python\\Python37\\share\\nltk_data'
    - 'C:\\Users\\16662\\AppData\\Local\\Programs\\Python\\Python37\\lib\\nltk_data'
    - 'C:\\Users\\16662\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
    - ''
**********************************************************************
```

# 解决办法

方法一：

直接尝试报错信息中的提示，先 import nltk，然后再 nltk.download('punkt')。

```python
import nltk
nltk.download('punkt')
```

（新建 py 文件运行，或者在 python console 中运行都可以，记得切换到项目所在的虚拟环境。）

如果报错的话，可以尝试方法二。

方法二：

访问nltk_data的github项目: https://github.com/nltk/nltk_data

将其整个下载下来，在其中的packages文件夹下可以找到所缺失的tokenizers文件夹

![](.01_Resource punkt not found_images/下载包.png)

将其解压缩，连同tokenizers文件夹放至报错的任一目录下即可

![](.01_Resource punkt not found_images/文件位置.png)

即在上图中任选一处，放置即可，若无nltk_data文件夹，则新建一个即可，如下图所示

比如可以放在目录：:~/miniconda3/envs/py310/nltk_data

类似的诸如“Resource averaged_perceptron_tagger not found”等等报错，可同样处理

# 参考

[1] 使用nltk时，报错Resource punkt not found, https://zhuanlan.zhihu.com/p/433423216