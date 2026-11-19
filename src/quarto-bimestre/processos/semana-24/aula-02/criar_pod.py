from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

pod = client.V1Pod(
    metadata=client.V1ObjectMeta(name='meu-nginx'),
    spec=client.V1PodSpec(
        containers=[
            client.V1Container(
                name='nginx',
                image='nginx:latest'
            )
        ]
    )
)

v1.create_namespaced_pod(
    namespace='default',
    body=pod
)

print('Pod criado!')