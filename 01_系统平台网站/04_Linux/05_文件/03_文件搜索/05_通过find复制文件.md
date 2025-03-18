你可以使用以下命令来完成这个任务：  

```bash
mkdir -p tmp_check10  # 先创建目标文件夹
find . -name "*_add_ref.json" | head -10 | xargs -I {} cp {} tmp_check10/
```

### 解释：
1. `mkdir -p tmp_check10`：创建 `tmp_check10` 文件夹（如果已存在，则不会报错）。
2. `find . -name "*_add_ref.json"`：查找当前目录及子目录中符合条件的文件。
3. `head -10`：只取前10个文件。
4. `xargs -I {} cp {} tmp_check10/`：将这10个文件拷贝到 `tmp_check10/` 目录下。

⚠️ **注意事项**：
- 如果文件名包含空格或特殊字符，`xargs` 可能会出问题。可以改用 `-print0` 和 `xargs -0` 处理：
  
  ```bash
  find . -name "*_add_ref.json" -print0 | head -10 -z | xargs -0 -I {} cp {} tmp_check10/
  ```

这样可以确保文件名被正确处理。