import docker


class DockerController:
    def __init__(self, base_url: str):
        self.client = docker.DockerClient(base_url=base_url)

    def list_running_containers(self):
        """
        查询所有的容器
        """
        return self.client.containers.list()

    def list_running_object_containers(self):
        """
        查询所有的容器，已List返回
        """
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
        """
        获取单个容器
        """
        return self.client.containers.get(container_id)

    def run_container(self, image, command=None, detach=True):
        """
        启动容器
        """
        return self.client.containers.run(image, command, detach=detach)

    def stop_container(self, container_id):
        """
        暂停容器
        """
        self.client.containers.get(container_id).stop()

    def remove_container(self, container_id):
        """
        删除容器
        """
        self.client.containers.get(container_id).remove()
