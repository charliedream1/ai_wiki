# 1. 安装

```shell
Ubuntu 或 Debian
apt-get install tmux
CentOS 或 Fedora
yum install tmux
Mac
brew install tmux
```

# 2. 命令

```text
Ctrl+b %	划分左右两个窗格。
Ctrl+b "	划分上下两个窗格。
Ctrl+b 上下左右箭头	多个窗格之间切换
Ctrl+b ;	光标切换到上一个窗格。
Ctrl+b o	光标切换到下一个窗格。
Ctrl+b {	当前窗格左移。
Ctrl+b }	当前窗格右移。
Ctrl+b Ctrl+o	当前窗格上移。
Ctrl+b Alt+o	当前窗格下移。
Ctrl+b x	关闭当前窗格。
Ctrl+b !	将当前窗格拆分为一个独立窗口。
Ctrl+b z	当前窗格全屏显示，再使用一次会变回原来大小。
Ctrl+b Ctrl+	按箭头方向调整窗格大小。
Ctrl+b q	显示窗格编号。
Ctrl+b :set synchronize-panes	多个窗格同步输入切换，设置一次同步输入，再设置一次关闭同步输入
```

绑定快捷键

比如上面的 同步输入命令太长了，就可以使用绑定快捷键实现简单的命令

```shell
vim ~/.tmux.conf
bind-key s setw synchronize-panes
source ~/.tmux.conf
```

让快捷键 Ctrl+b s快捷键来实现窗格同步输入的切换。试下 Ctrl+b s 代替了 
Ctrl+b :set synchronize-panes 实现了同步输入。

# 参考

[1] tmux使用--同步多终端输入, https://blog.csdn.net/feifeixiang2835/article/details/107051741