网址：https://docs.anaconda.com/miniconda/install/#quick-command-line-install

linux下命令行安装miniconda
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

windows下命令行安装miniconda
```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S
del .\miniconda.exe
```

windows下powershell安装miniconda
```bash
wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -outfile ".\miniconda.exe"
Start-Process -FilePath ".\miniconda.exe" -ArgumentList "/S" -Wait
del .\miniconda.exe
```

安装完后，需要重启终端，然后就可以使用conda命令了。(注意，下面的路径在windows下可能是condabin)

```bash
source ~/miniconda3/bin/activate
```

在所有终端初始化conda（如果无法执行，可以打开Anaconda Prompt命令窗口或者git bash命令窗口操作）
```bash
conda init --all
```

注意：windows下若始终无法开启conda环境，可以从按照的开始菜单的程序conda里的Anaconda Powershell启动