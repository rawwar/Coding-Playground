from openai import OpenAI

client = OpenAI(api_key="<INSERT KEY HERE>")

# Create index
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=True,
    verify_certs=True,
    ssl_show_warn=False,
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

response = client.indices.create(index="vec_test", body=index_settings)

print(response)


# Insert docs


docs = ["I am a software engineer", "I am a data scientist"]


for each in docs:
    res = client.embeddings.create(input=each, model="text-embedding-ada-002")

    document = {
        "my_vector": res.data[0].embedding,
        "my_text": each,
    }

    response = client.index(index="vec_test", body=document, refresh=True)

    print(response)


## Search

text = "Data scientist"
res = client.embeddings.create(input=text, model="text-embedding-ada-002")
query = {"size":2,"query":{"knn":{"my_vector":{"vector":res.data[0].embedding,"k":2}}}}
# Perform the search
response = client.search(index="vec_test", body=query)

# Print the response
print(response)

