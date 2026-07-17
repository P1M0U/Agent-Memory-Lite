"""Hermes 插件入口 — 后向兼容薄层

逻辑已迁移到 agent_memory_lite.plugins.hermes.provider。
本文件仅供 Hermes 的 plugin.yaml 加载入口使用。
"""

from agent_memory_lite.plugins.hermes.provider import (
    AgentMemoryLiteProvider,
    register,
)

__all__ = ["AgentMemoryLiteProvider", "register"]
