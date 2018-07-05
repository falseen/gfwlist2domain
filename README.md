# gfwlist2domain
> 获取gfwlist中的域名，去掉里面的白名单以及重复网址，只保留google.com这样的一级域名

# 说明
* builtin.txt 是自己预留的黑名单
* -i 输入的gfwlist.txt，默认同级目录下的 gfwlist.txt
* -o 输出的文件，默认同级目录下的 domain.txt
* gwflist.txt 获取地址是 https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt
* scp pac.conf root@192.168.31.1:/etc/misstar/applications/ss/config/pac.conf
