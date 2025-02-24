**Github无法拉取的解决方法**

https://gitclone.com/

方法一（替换URL）

git clone https://gitclone.com/github.com/tendermint/tendermint.git

方法二（设置git参数）

git config --global url."https://gitclone.com/".insteadOf https://

git clone https://github.com/tendermint/tendermint.git

方法三（使用cgit客户端）

cgit clone https://github.com/tendermint/tendermint.git

**实测**

有些可以解决，有些不行
