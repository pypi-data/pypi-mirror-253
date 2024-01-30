## trans client 

### Introduction

​	A tool based on scp for quickly transmitting data on a server. If you

do not want to enter the account password during the transmission process,

please configure the ssh key in advance. This is a client-side script. If

you have set up your own LAN server as a backup server or data transfer

station, you can install the trans-server script on the server side.



### Install

```shell
pip install trans-client
```



### Usage

#### help
```shell
tcl help
```
#### config

```shell
tcl config
```
> user:     remote user
> ip:       remote host ip
> path:     the base path that you want to use
#### login
```shell
tcl login
```
> ssh user@ip

#### Trans

some examples:
- if you config like this
  ```json
  user: jack
  ip:   192.168.3.2
  path: /home/jack
  ```
  
- get file/dir from remote server

  `tcl --get /home/local/dir remote_dir` or `tcl -g /home/local/dir remote_dir`

    > scp -r jack@192.168.3.2:/home/jcak/remote_dir /home/local/dir

- upload file/dir to remote server
  `tcl --put /home/local/dir remote_dir` or `tcl -p /home/local/dir remote_dir`
    > scp -r /home/local/dir jack@192.168.3.2:/home/jcak/remote_dir

#### clean

>   clean the ~/.trans.cfg

```shell
tcl clean
```



## Contact me

zhewei@stu.xidian.edu.cn



## License

trans-client is provided under the [MIT LICENSE](./LICENSE)