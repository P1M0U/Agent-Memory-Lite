"""jieba 中文分词封装"""

from pathlib import Path

import jieba

# 加载自定义词典（如果存在）
_DICT_PATH = Path(__file__).parent.parent / "dicts" / "tech_terms.txt"
if _DICT_PATH.exists():
    jieba.load_userdict(str(_DICT_PATH))


def tokenize(text: str) -> str:
    """jieba 分词，返回空格分隔的词语"""
    return " ".join(jieba.cut(text))


def tokenize_list(text: str) -> list[str]:
    """jieba 分词，返回词语列表"""
    return list(jieba.cut(text))
