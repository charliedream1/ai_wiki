# Copyright (c) Alibaba, Inc. and its affiliates.
from enum import Enum

DEFAULT_ROOT_CACHE_DIR = '~/.cache/llmuses'


class DumpMode:
    OVERWRITE = 'overwrite'
    APPEND = 'append'


class MetricsConstant:
    EPSILON = float(1e-6)
    INVALID_VALUE = -9999999
    ROUGE_KEYS = [
        'rouge-1-r',
        'rouge-1-p',
        'rouge-1-f',
        'rouge-2-r',
        'rouge-2-p',
        'rouge-2-f',
        'rouge-l-r',
        'rouge-l-p',
        'rouge-l-f',
    ]


class MetricMembers(Enum):

    # Math accuracy metric
    MATH_ACCURACY = 'math_accuracy'

    # Code pass@k metric
    CODE_PASS_K = 'code_pass_k'

    # Code rouge metric
    ROUGE = 'rouge'

    # ELO rating system for pairwise comparison
    ELO = 'elo'

    # Pairwise comparison win/lose and tie(optional)
    PAIRWISE = 'pairwise'

    # Rating score for single model
    SCORE = 'score'


class ArenaWinner:

    MODEL_A = 'model_a'

    MODEL_B = 'model_b'

    TIE = 'tie'

    TIE_BOTH_BAD = 'tie_both_bad'

    UNKNOWN = 'unknown'


class ArenaMode:
    SINGLE = 'single'
    PAIRWISE = 'pairwise'
    PAIRWISE_BASELINE = 'pairwise_baseline'


class OutputsStructure:

    LOGS_DIR = 'logs_dir'

    PREDICTIONS_DIR = 'predictions_dir'

    REVIEWS_DIR = 'reviews_dir'

    REPORTS_DIR = 'reports_dir'

    CONFIGS_DIR = 'configs_dir'


class AnswerKeys:

    ANSWER_ID = 'answer_id'

    RAW_INPUT = 'raw_input'

    ORIGIN_PROMPT = 'origin_prompt'

    MODEL_SPEC = 'model_spec'

    SUBSET_NAME = 'subset_name'

    CHOICES = 'choices'


class ReviewKeys:

    REVIEW_ID = 'review_id'

    REVIEWED = 'reviewed'

    REVIEWER_SPEC = 'reviewer_spec'

    REVIEW_TIME = 'review_time'

    MESSAGE = 'message'

    CONTENT = 'content'

    GOLD = 'gold'

    PRED = 'pred'

    RESULT = 'result'

    REVIEW = 'review'


class EvalConfigKeys:
    CLASS_REF = 'ref'
    CLASS_ARGS = 'args'
    ENABLE = 'enable'
    POSITION_BIAS_MITIGATION = 'position_bias_mitigation'
    RANDOM_SEED = 'random_seed'
    FN_COMPLETION_PARSER = 'fn_completion_parser'
    COMPLETION_PARSER_KWARGS = 'completion_parser_kwargs'
    OUTPUT_FILE = 'output_file'
    MODEL_ID_OR_PATH = 'model_id_or_path'
    MODEL_REVISION = 'revision'
    GENERATION_CONFIG = 'generation_config'
    PRECISION = 'precision'
    TEMPLATE_TYPE = 'template_type'


class FnCompletionParser:
    LMSYS_PARSER: str = 'lmsys_parser'
    RANKING_PARSER: str = 'ranking_parser'


class PositionBiasMitigation:
    NONE = 'none'
    RANDOMIZE_ORDER = 'randomize_order'
    SWAP_POSITION = 'swap_position'


class EvalStage:
    # Enums: `all`, `infer`, `review`
    ALL = 'all'
    INFER = 'infer'
    REVIEW = 'review'
