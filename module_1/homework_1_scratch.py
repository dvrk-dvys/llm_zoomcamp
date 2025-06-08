#Question 1
#Run Elastic Search 8.17.6, and get the cluster information. If you run it on localhost, this is how you do it:

#How its done int notebook
from elasticsearch import Elasticsearch

es_client = Elasticsearch(
    "http://localhost:9200"
)

print(es_client.info())
#Docker
#docker network create elastic
#docker pull docker.elastic.co/elasticsearch/elasticsearch:8.17.6
#docker rm -f es01

#docker run -d \
#  --name es01 \
#  --net elastic \
#  -p 9200:9200 \
#  -p 9300:9300 \
#  -e "discovery.type=single-node" \
#  -e "xpack.security.enabled=false" \
#  -m 6GB \
#  -it docker.elastic.co/elasticsearch/elasticsearch:8.17.6


#❯ curl localhost:9200

#{
#  "name" : "eb5d27e855bd",
#  "cluster_name" : "docker-cluster",
#  "cluster_uuid" : "swAeNUvnQR2O9vLPDCMbfw",
#  "version" : {
#    "number" : "8.17.6",
#    "build_flavor" : "default",
#    "build_type" : "docker",
#!!!!!    "build_hash" : "dbcbbbd0bc4924cfeb28929dc05d82d662c527b7",
#    "build_date" : "2025-04-30T14:07:12.231372970Z",
#    "build_snapshot" : false,
#    "lucene_version" : "9.12.0",
#    "minimum_wire_compatibility_version" : "7.17.0",
#    "minimum_index_compatibility_version" : "7.0.0"
#  },
#  "tagline" : "You Know, for Search"
#}
#___________________________________________________________________________________

#Question 2
#from tqdm.auto import tqdm

#index_settings = {
#    "settings": {
#        "number_of_shards": 1,
#        "number_of_replicas": 0
#    },
#    "mappings": {
#        "properties": {
#            "text": {"type": "text"},
#            "section": {"type": "text"},
#            "question": {"type": "text"},
#            "course": {"type": "keyword"}
#        }
#    }
#}

#index_name  = "course-questions"
#es_client.indices.create(index=index_name, body=index_settings)

#for doc in tqdm(documents):
#    es_client.index(index=index_name, document=doc)
#___________________________________________________________________________________
#Question 3
#___________________
#Score:  44.50556
#Answer:  {'text': 'Launch the container image in interactive mode and overriding the entrypoint, so that it starts a bash command.\ndocker run -it --entrypoint bash <image>\nIf the container is already running, execute a command in the specific container:\ndocker ps (find the container-id)\ndocker exec -it <container-id> bash\n(Marcos MJD)', 'section': '5. Deploying Machine Learning Models', 'question': 'How do I debug a docker container?', 'course': 'machine-learning-zoomcamp'}
#___________________________________________________________________________________

#Question 4
#___________________
#How do I debug a docker container?
#Kubernetes-dashboard
#How do I copy files from a different folder into docker container’s working directory?