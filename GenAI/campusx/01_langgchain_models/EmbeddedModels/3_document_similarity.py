from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()


embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=300
)



documents = [
    "New Delhi is the capital of India",
    "Moscow is the capital of Russia",
    "Tokyo is the capital of Japan",
    "Seoul is the capital of South Korea"
]


query = "Tell me where is Moscow?"



doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)



# Now we find the similarity
# Here we only take the 0th element from the list as that's wahy required
scores = cosine_similarity([query_embedding], doc_embeddings)[0]


# Here we convert the scores into enumerable list
print(list(enumerate(scores)))

"""
output: [(0, np.float64(0.17629815339876925)), 
(1, np.float64(0.6001285539712825)), 
(2, np.float64(0.23432499713310784)), 
(3, np.float64(0.22516103331231563))]

0th element is index
1th element in similarity score
"""



# And then we sort it based on the similarity score (ascending order)
print(sorted(list(enumerate(scores)), key=lambda x:x[1]))



# We extract only the biggest one
print(sorted(list(enumerate(scores)), key=lambda x:x[1])[-1])



index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]


print("\n")
print(query)
print(documents[index])
print("\nSimilarity score is: ", score)

"""
output:

Tell me where is Moscow?
Moscow is the capital of Russia

Similarity score is:  0.6001285539712825
"""
