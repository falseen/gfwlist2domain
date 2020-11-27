# gfwlist2domain
> 自动获取gfwlist中的域名，去掉里面的白名单以及重复网址，只保留google.com这样的一级域名

# 说明
* builtin.txt 是自己预留的域名，会自动加入domain.txt中
* 每次运行都会获取最新的 gfwlist.txt ，不用手动修改。
* 输出的文件在同级目录下的 domain.txt
* gwflist.txt 获取地址是 https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt
* scp pac.conf root@192.168.31.1:/etc/misstar/applications/ss/config/pac.conf
* 本项目fork自https://github.com/dhso/gfwlist2domain，在其基础上做了一些修改。
