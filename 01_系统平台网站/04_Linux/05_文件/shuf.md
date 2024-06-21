# 使用
ps:

shuf train.txt -o test.txt -n 30

从train.txt文件中随机读取30行文本输出到test.txt

```text
shuf --help
用法： shuf [选项]... [文件]
　或者:  shuf -e [选项]... [参数]...
　或者:  shuf -i LO-HI [选项]...
Write a random permutation of the input lines to standard output.

如果没有指定文件，或者文件为"-"，则从标准输入读取。

必选参数对长短选项同时适用。
  -e, --echo                treat each ARG as an input line
  -i, --input-range=LO-HI   treat each number LO through HI as an input line
  -n, --head-count=COUNT    output at most COUNT lines
  -o, --output=FILE         write result to FILE instead of standard output
      --random-source=FILE  get random bytes from FILE
  -r, --repeat              output lines can be repeated
  -z, --zero-terminated     line delimiter is NUL, not newline
      --help        显示此帮助信息并退出
      --version        显示版本信息并退出

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
请向<http://translationproject.org/team/zh_CN.html> 报告shuf 的翻译错误
Full documentation at: <http://www.gnu.org/software/coreutils/shuf>
or available locally via: info '(coreutils) shuf invocation'
```

# 参考

[1] inux 命令shuf，https://www.cnblogs.com/yangwithtao/p/7047988.html