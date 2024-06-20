# 使用心得

- 优点：可以标记页码
- 问题：PDF转markdown会导致原始结构无法保留，特别是表格和标题结构容易丢失

# 1. 资源

- 使用文档：https://pymupdf.readthedocs.io/en/latest/rag.html

# 2. 使用
## 2.1 PDF转Markdown

```bash
pip install -U pymupdf4llm
```

New features as of v0.0.2:

Support for pages with multiple text columns.

Support for image and vector graphics extraction:

Specify pymupdf4llm.to_markdown("input.pdf", write_images=True). Default is False.
Each image or vector graphic on the page will be extracted and stored as a PNG image named "input.pdf-pno-index.png" in the folder of "input.pdf". Where pno is the 0-based page number and index is some sequence number.
The image files will have width and height equal to the values on the page.
Any text contained in the images or graphics will not be extracted, but become visible as image parts.
Support for page chunks: Instead of returning one large string for the whole document, a list of dictionaries can be generated: one for each page. Specify data = pymupdf4llm.to_markdown("input.pdf", page_chunks=True). Then, for instance the first item, data[0] will contain a dictionary for the first page with the text and some metadata.

As a first example for directly supporting LLM / RAG consumers, this version can output LlamaIndex documents:

```python
import pymupdf4llm

md_text = pymupdf4llm.to_markdown("input.pdf")

# now work with the markdown text, e.g. store as a UTF8-encoded file
import pathlib
pathlib.Path("output.md").write_bytes(md_text.encode())
```

```python
import pymupdf4llm

md_read = LlamaMarkdownReader()
data = md_read.load_data("input.pdf")

# The result 'data' is of type List[LlamaIndexDocument]
# Every list item contains metadata and the markdown text of 1 page.
```

- A LlamaIndex document essentially corresponds to Python dictionary, where the markdown text of the page is one of the dictionary values. For instance the text of the first page is the the value of data[0].to_dict().["text"].
- For details, please consult LlamaIndex documentation.
- Upon creation of the LlamaMarkdownReader all necessary LlamaIndex-related imports are executed. Required related package installations must have been done independently and will not be checked during pymupdf4llm installation.

## 2.2 结合langchain分块

```python
import pymupdf4llm
from langchain.text_splitter import MarkdownTextSplitter

# Get the MD text
md_text = pymupdf4llm.to_markdown("input.pdf")  # get markdown for all pages

splitter = MarkdownTextSplitter(chunk_size=40, chunk_overlap=0)

splitter.create_documents([md_text])
```
