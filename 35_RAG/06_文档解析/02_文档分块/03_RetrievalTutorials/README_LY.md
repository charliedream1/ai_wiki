code from: https://github.com/FullStackRetrieval-com/RetrievalTutorials.git

使用prompt: https://smith.langchain.com/hub/wfh/proposal-indexing?organizationId=50995362-9ea0-4378-ad97-b4edae2f9f22

论文：
@misc{chen2023dense,
      title={Dense X Retrieval: What Retrieval Granularity Should We Use?},
      author={Tong Chen and Hongwei Wang and Sihao Chen and Wenhao Yu and Kaixin Ma and Xinran Zhao and Hongming Zhang and Dong Yu},
      year={2023},
      eprint={2312.06648},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```text
ChatPromptTemplate
Edit in Playground
SYSTEM

Decompose the "Content" into clear and simple propositions, ensuring they are interpretable out of

context.

1. Split compound sentence into simple sentences. Maintain the original phrasing from the input

whenever possible.

2. For any named entity that is accompanied by additional descriptive information, separate this

information into its own distinct proposition.

3. Decontextualize the proposition by adding necessary modifier to nouns or entire sentences

and replacing pronouns (e.g., "it", "he", "she", "they", "this", "that") with the full name of the

entities they refer to.

4. Present the results as a list of strings, formatted in JSON.



Example:



Input: Title: ¯Eostre. Section: Theories and interpretations, Connection to Easter Hares. Content:

The earliest evidence for the Easter Hare (Osterhase) was recorded in south-west Germany in

1678 by the professor of medicine Georg Franck von Franckenau, but it remained unknown in

other parts of Germany until the 18th century. Scholar Richard Sermon writes that "hares were

frequently seen in gardens in spring, and thus may have served as a convenient explanation for the

origin of the colored eggs hidden there for children. Alternatively, there is a European tradition

that hares laid eggs, since a hare’s scratch or form and a lapwing’s nest look very similar, and

both occur on grassland and are first seen in the spring. In the nineteenth century the influence

of Easter cards, toys, and books was to make the Easter Hare/Rabbit popular throughout Europe.

German immigrants then exported the custom to Britain and America where it evolved into the

Easter Bunny."

Output: [ "The earliest evidence for the Easter Hare was recorded in south-west Germany in

1678 by Georg Franck von Franckenau.", "Georg Franck von Franckenau was a professor of

medicine.", "The evidence for the Easter Hare remained unknown in other parts of Germany until

the 18th century.", "Richard Sermon was a scholar.", "Richard Sermon writes a hypothesis about

the possible explanation for the connection between hares and the tradition during Easter", "Hares

were frequently seen in gardens in spring.", "Hares may have served as a convenient explanation

for the origin of the colored eggs hidden in gardens for children.", "There is a European tradition

that hares laid eggs.", "A hare’s scratch or form and a lapwing’s nest look very similar.", "Both

hares and lapwing’s nests occur on grassland and are first seen in the spring.", "In the nineteenth

century the influence of Easter cards, toys, and books was to make the Easter Hare/Rabbit popular

throughout Europe.", "German immigrants exported the custom of the Easter Hare/Rabbit to

Britain and America.", "The custom of the Easter Hare/Rabbit evolved into the Easter Bunny in

Britain and America."]

HUMAN

Decompose the following:

{input}
```

使用

```python
# set the LANGCHAIN_API_KEY environment variable (create key in settings)
from langchain import hub
prompt = hub.pull("wfh/proposal-indexing")
```