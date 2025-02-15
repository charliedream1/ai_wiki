实测加入meta条件过滤，只有在1个条件时才能生效，多个条件的时候无法生效

```python
from langchain_chroma import Chroma

vectorstore = Chroma(persist_directory=vec_db_path, 
                     embedding_function=embed_mdl_client,
                     collection_name=vec_db_name)

retriever = vectorstore.as_retriever(search_type="similarity_score_threshold",
                                    search_kwargs={"k": args.top_k,
                                        'score_threshold': args.threshold})
documents = retriever.invoke(query, filter={"country": queries.country})
```