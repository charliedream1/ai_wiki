# 1. 方法

通过大模型和llama-index的DatasetGenerator构建问答数据集。

```python
import nest_asyncio

nest_asyncio.apply()

from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
)
from llama_index.evaluation import (
    DatasetGenerator,
    FaithfulnessEvaluator,
    RelevancyEvaluator
)
from llama_index.llms import OpenAI

import openai
import time

openai.api_key = 'OPENAI-API-KEY'

# Download Data
!mkdir -p 'data/10k/'
!wget 'https://raw.githubusercontent.com/jerryjliu/llama_index/main/docs/examples/data/10k/uber_2021.pdf' -O 'data/10k/uber_2021.pdf'

# Load Data
reader = SimpleDirectoryReader("./data/10k/")
documents = reader.load_data()

# To evaluate for each chunk size, we will first generate a set of 40 questions from first 20 pages.
eval_documents = documents[:20]
data_generator = DatasetGenerator.from_documents()
eval_questions = data_generator.generate_questions_from_nodes(num = 20)

# We will use GPT-4 for evaluating the responses
gpt4 = OpenAI(temperature=0, model="gpt-4")

# Define service context for GPT-4 for evaluation
service_context_gpt4 = ServiceContext.from_defaults(llm=gpt4)

# Define Faithfulness and Relevancy Evaluators which are based on GPT-4
faithfulness_gpt4 = FaithfulnessEvaluator(service_context=service_context_gpt4)
relevancy_gpt4 = RelevancyEvaluator(service_context=service_context_gpt4)

# Define function to calculate average response time, average faithfulness and average relevancy metrics for given chunk size
def evaluate_response_time_and_accuracy(chunk_size):
    total_response_time = 0
    total_faithfulness = 0
    total_relevancy = 0

    # create vector index
    llm = OpenAI(model="gpt-3.5-turbo")
    service_context = ServiceContext.from_defaults(llm=llm, chunk_size=chunk_size)
    vector_index = VectorStoreIndex.from_documents(
        eval_documents, service_context=service_context
    )

    query_engine = vector_index.as_query_engine()
    num_questions = len(eval_questions)

    for question in eval_questions:
        start_time = time.time()
        response_vector = query_engine.query(question)
        elapsed_time = time.time() - start_time
        
        faithfulness_result = faithfulness_gpt4.evaluate_response(
            response=response_vector
        ).passing
        
        relevancy_result = relevancy_gpt4.evaluate_response(
            query=question, response=response_vector
        ).passing

        total_response_time += elapsed_time
        total_faithfulness += faithfulness_result
        total_relevancy += relevancy_result

    average_response_time = total_response_time / num_questions
    average_faithfulness = total_faithfulness / num_questions
    average_relevancy = total_relevancy / num_questions

    return average_response_time, average_faithfulness, average_relevancy

# Iterate over different chunk sizes to evaluate the metrics to help fix the chunk size.
for chunk_size in [128, 256, 512, 1024, 2048]
  avg_time, avg_faithfulness, avg_relevancy = evaluate_response_time_and_accuracy(chunk_size)
  print(f"Chunk size {chunk_size} - Average Response time: {avg_time:.2f}s, Average Faithfulness: {avg_faithfulness:.2f}, Average Relevancy: {avg_relevancy:.2f}")
  
```


# 参考

[1] Evaluating the Ideal Chunk Size for a RAG System using LlamaIndex, https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5
