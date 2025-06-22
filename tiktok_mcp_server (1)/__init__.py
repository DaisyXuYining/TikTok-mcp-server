"""
TikTok MCP Server - TikTok无水印视频下载并提取文本的 MCP 服务器

该包提供了一个基于Model Context Protocol (MCP)的服务器，
可以从TikTok分享链接下载无水印视频，提取音频并转换为文本。

主要功能：
- 从TikTok分享链接获取无水印视频
- 自动提取视频音频  
- 使用AI语音识别提取文本内容
- 自动清理中间临时文件
- 支持自定义API配置

作者: MiniMax Agent
版本: 1.0.0
许可证: MIT
"""

__version__ = "1.0.0"
__author__ = "MiniMax Agent"
__email__ = "agent@minimax.com"

from .server import main

__all__ = ["main"]
