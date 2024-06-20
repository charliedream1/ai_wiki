# 使用

```python
from langchain.text_splitter import MarkdownHeaderTextSplitter

markdown_document = "# Foo\n\n    ## Bar\n\nHi this is Jim\n\nHi this is Joe\n\n ### Boo \n\n Hi this is Lance \n\n ## Baz\n\n Hi this is Molly"

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_header_splits = markdown_splitter.split_text(markdown_document)
for split in md_header_splits:
    print(split)
```

# 参考

[1] MarkdownHeaderTextSplitter，https://python.langchain.com.cn/docs/modules/data_connection/document_transformers/text_splitters/markdown_header_metadata