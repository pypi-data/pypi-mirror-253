<h1 align="center">tt_util</h1>

此项目是根据[@buyfakett](https://github.com/buyfakett)的python使用习惯自己封装打包的包

- yaml_util.py

yaml的各种封装方法，主要使用read_yaml方法，来读取配置，所有配置都放在启动文件同一目录的config文件夹下，传入的filename不需要加.yaml

- uuid_util.py

把uuid的第一个值提取出来，做一层文件夹，可以让oss上快速查询和把第一层文件夹给去掉

- svn_util.py

操作svn的各种封装方法，使用示例：

```python
# 使用示例
svn_client = SVNClient(repo_url='svn://', working_copy_path='', username='',
                       password='')
checkout_output, checkout_error, checkout_code = svn_client.checkout()
logging.info(f'检出日志: {checkout_output}')
logging.error(f'检出错误: {checkout_error}')
logging.info(f'检出返回码: {checkout_code}')

update_output, update_error, update_code = svn_client.update()
logging.info(f'更新日志: {update_output}')
logging.error(f'更新错误: {update_error}')
logging.info(f'更新返回码: {update_code}')

add_output, add_error, add_code = svn_client.add("/app/temp/svn/nginx/2")
logging.info(f'增加日志: {add_output}')
logging.error(f'增加错误: {add_error}')
logging.info(f'增加返回码: {add_code}')

commit_output, commit_error, commit_code = svn_client.commit('Committing changes')
logging.info(f'提交日志: {commit_output}')
logging.error(f'提交错误: {commit_error}')
logging.info(f'提交返回码: {commit_code}')
```

- ssh_util.py

ssh到服务器的各种封装方法，使用示例：

```python
host = ''
password = ''

ssh = SSHClient(host, password)

# 执行单行命令
result_single = ssh.execute_command('ls -l')

# 执行多行命令
commands = ['pwd', 'whoami']
result_multiple = ssh.execute_commands(commands)

# 上传并执行脚本
local_script_path = 'C:\\Users\\buyfakett\\Desktop\\1.sh'
remote_script_path = '/root/1.sh'
result_script = ssh.upload_and_execute_script(local_script_path, remote_script_path)

ssh.close()
```

- exec_shell.py

在当前运行的服务器上运行命令和在服务器上检测文件，使用示例：

```python
exec_shell('mkdir /test')

check_file('/data', '1*')
```

- aes_util.py

aes非对称加密的各种封装方法，使用示例：

```python
key = '12223'
data = 'hc刺激啊四神聪骄傲i'
encrypt = encrypt_aes(data, key)
print(encrypt)
print(decrypt_aes(encrypt, key))
```

- qiniu_util.py

七牛云oss封装，使用示例：

```python
# 上传
qiniu = QiniuFunction()
ret, info = qiniu.upload_file(local_file, remote_file)
```

- check_domain.py

检测域名是否做了dns解析，使用示例：

```python
if not check_domain(domain):
	return resp_400()
else:
	return resp_200()
```

- docker_util.py

检测/控制docker，使用示例：

```python
# 当前运行的服务
remote_host = "tcp://192.168.1.1:2375"
test = DockerController(remote_host)
print(f"总共有这些服务正在运行：{test.list_running_object_containers()}")

# 暂停容器
test.stop_container('postgres')

# 删除容器
test.remove_container('postgres')

# 获取单个容器
test.inspect_container('postgres')
```

