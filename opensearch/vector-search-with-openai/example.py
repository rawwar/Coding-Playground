from openai import OpenAI

INDEX_NAME = "test-index-2"
docs = ["I am a software engineer", "I am a data scientist"]

client_oai = OpenAI(api_key="<OPENAI_KEY>")

# Create index
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=True,
    verify_certs=False
)

# Define the index settings and mappings
index_settings = {
    "settings": {
        "index": {"knn": True, "number_of_shards": 1, "number_of_replicas": 0}
    },
    "mappings": {
        "properties": {
            "my_vector": {
                "type": "knn_vector",
                "dimension": 1536,
                "method": {"name": "hnsw", "space_type": "l2", "engine": "faiss"},
            }
        }
    },
}

response = client.indices.create(index=INDEX_NAME, body=index_settings)

print(response)


# Insert docs





for each in docs:
    res = client_oai.embeddings.create(input=each, model="text-embedding-ada-002")

    document = {
        "my_vector": res.data[0].embedding,
        "my_text": each,
    }

    response = client.index(index=INDEX_NAME, body=document, refresh=True)

    print(response)






## Search

text = "Data scientist"
res = client_oai.embeddings.create(input=text, model="text-embedding-ada-002")
query = {"size":1,"query":{"knn":{"my_vector":{"vector":res.data[0].embedding,"k":2}}}}
# Perform the search
response = client.search(index=INDEX_NAME, body=query)

# Print the response
print(response)

