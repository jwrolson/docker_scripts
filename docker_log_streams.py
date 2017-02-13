import json
import docker

def main():
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    streams = []
    streams.append(client.events())
    for contrainer in client.containers.list():
        log_kwargs = {}
        log_kwargs['stdout'] = True
        log_kwargs['stderr'] = True
        log_kwargs['timestamps'] = True
        log_kwargs['stream'] = True
        streams.append(contrainer.logs(**log_kwargs))
    for stream in streams:
        for line in stream:
            print(line)

if __name__ == '__main__':
    main()
