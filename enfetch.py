import docker, pyaml

client = docker.from_env(version="auto")
containers = client.containers.list()

yml = {
  'version': '2',
  'services': {}
}

for container in containers:
  service_name = container.attrs['Config']['Labels']['com.docker.compose.service']
  yml['services'][service_name] = { 'environment': {} }

  envs = {}
  for env in container.attrs['Config']['Env']:
    chunks = env.split('=', 1)
    yml['services'][service_name]['environment'][chunks[0]] = chunks[1]

pyaml.pprint(yml)
