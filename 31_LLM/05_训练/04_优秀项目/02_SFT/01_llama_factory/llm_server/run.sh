#!/bin/bash

export LD_PRELOAD=$LD_PRELOAD:/usr/local/python3.10.13/lib/python3.10/site-packages/sklearn/utils/../../scikit_learn.libs/libgomp-d22c30c5.so.1.0.0
ASCEND_RT_VISIBLE_DEVICES=1,2 API_PORT=62 llamafactory-cli api qwen2_7B_Instruct.yaml
