# 问题

```bash
$ git checkout https://github.com/openai/human-eval
$ pip install -e human-eval
```

get probelm

```text
ERROR: human-eval is not a valid editable requirement. It should either be a path to a local project or a VCS URL (beginning with bzr+http, bzr+https, bzr+ssh, bzr+sftp, bzr+ftp, bzr+lp, bzr+file, git+http, git+https, git+ssh, git+git, git+file, hg+file, hg+http, hg+https, hg+ssh, hg+static-http, svn+ssh, svn+http, svn+https, svn+svn, svn+file).
```

# 解决

```bash
pip install human-eval
```