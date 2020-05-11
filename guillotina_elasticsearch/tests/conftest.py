from guillotina_elasticsearch import ES_CLIENT_VERSION
from pytest_docker_fixtures import images


if ES_CLIENT_VERSION.minor > 6:
    image_version = "7.5.1"
else:
    image_version = "6.4.3"

images.configure(
    "elasticsearch",
    "docker.elastic.co/elasticsearch/elasticsearch",
    image_version,
    env={
        "xpack.security.enabled": None,  # unset
        "discovery.type": "single-node",
        "http.host": "0.0.0.0",
        "transport.host": "127.0.0.1",
    },
)


pytest_plugins = [
    "pytest_docker_fixtures",
    "guillotina.tests.fixtures",
    "guillotina_elasticsearch.tests.fixtures",
]
