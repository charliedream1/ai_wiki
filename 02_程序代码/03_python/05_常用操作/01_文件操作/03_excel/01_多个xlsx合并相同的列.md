```python
import pandas as pd
import glob

def merge_excel_files(file_path, output_file):
    """
    合并指定路径下所有 Excel 文件中的相同列，并保存为新的 Excel 文件。

    :param file_path: 要合并的 Excel 文件的路径，支持通配符
    :param output_file: 合并后保存的 Excel 文件名
    """
    # 获取所有符合条件的文件路径
    files = glob.glob(file_path)

    # 定义一个空的列表来存储每个 DataFrame
    dataframes = []

    # 循环遍历每个文件
    for file in files:
        df = pd.read_excel(file)
        dataframes.append(df)

    # 获取所有 DataFrame 的共同列
    common_columns = set.intersection(*(set(df.columns) for df in dataframes))

    # 合并所有 DataFrame 中的共同列
    merged_data = pd.concat([df[list(common_columns)] for df in dataframes], ignore_index=True)

    # 将合并结果保存到新的 Excel 文件
    merged_data.to_excel(output_file, index=False)
    print(f"合并完成，结果已保存到 '{output_file}'")

# 示例调用
merge_excel_files('path/to/your/files/*.xlsx', 'merged_output.xlsx')

```

使用说明：

函数定义：merge_excel_files 函数接收两个参数：

file_path：要合并的 Excel 文件的路径，可以使用通配符。

output_file：合并后保存的 Excel 文件名。

示例调用：你可以用实际的路径替换 path/to/your/files/*.xlsx，并指定合并后文件的名称。

确保安装了 pandas 和 openpyxl，并在合适的环境中运行该代码。
