from retrying import retry
from huggingface_hub import snapshot_download

MAX_TRY_NUM = 10


@retry(stop_max_attempt_number=MAX_TRY_NUM)
def download(repo_id, cache_dir, repo_type):
    snapshot_download(repo_id=repo_id,
                      cache_dir=cache_dir,
                      repo_type=repo_type)


def main():
    # 1. sometimes it will fail, try several times
    # 2. it supports continue downloading
    # 3. it's much faster than git clone
    # repo_id = 'YeungNLP/moss-003-sft-data'
    # repo_id = 'BAAI/bge-large-zh-v1.5'
    repo_id = 'BAAI/bge-reranker-large'
    cache_dir = 'D:\\mdl'
    repo_type = "model"   # dataset, model
    download(repo_id, cache_dir, repo_type)


if __name__ == '__main__':
    main()
