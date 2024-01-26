# -*- coding: utf-8 -*-            
# @Author : buyfakett
# @Time : 2024/1/25 20:02
import docker


class DockerController:
    def __init__(self, base_url: str):
        self.client = docker.DockerClient(base_url=base_url)

    def running_containers(self):
        return self.client.containers.list()

    def list_running_containers(self):
        container_list = []
        for container in self.client.containers.list():
            container_list.append({
                'id': container.short_id,
                'name': container.name,
                'status': container.status,
                'image': container.image,
            })
        return container_list

    def inspect_container(self, container_id):
        return self.client.containers.get(container_id)

    def run_container(self, image, command=None, detach=True):
        return self.client.containers.run(image, command, detach=detach)

    def stop_container(self, container_id):
        self.client.containers.get(container_id).stop()

    def remove_container(self, container_id):
        self.client.containers.get(container_id).remove()