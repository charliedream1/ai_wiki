查看系统是否支持avx512

```bash
grep avx /proc/cpuinfo
# 或者
grep avx2 /proc/cpuinfo
# 或者
grep -o 'avx' /proc/cpuinfo
# 或者
lscpu | grep 'avx'
```
