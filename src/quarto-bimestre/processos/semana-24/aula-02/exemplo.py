from kubernetes import config, client

config.load_kube_config()

v1 = client.CoreV1Api()

print('Conectado ao cluster!')

for node in v1.list_node().items:
    print(node.metadata.name)