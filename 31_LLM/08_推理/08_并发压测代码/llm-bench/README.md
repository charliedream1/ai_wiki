# BentoCloud Benchmark Client

## Usage

### 1. Set up environment variables

Make sure you have logged into Huggingface

```bash
huggingface-cli login
```

Set environment variables for benchmarking

```bash
export BASE_URL=<BentoCloud Service URL>
export SYSTEM_PROMPT=1      // 1 or 0
```

### 2. Run benchmark

```bash
python benchmark.py --max_users 10 --session_time 300 --ping_correction
```


- `max_users` is the max number of concurrent users to spawn
- `session_time` is the duration of the benchmark sesssion, in seconds
- `ping_correction` is a flag that determines whether ping latency should be deducted from the metrics
