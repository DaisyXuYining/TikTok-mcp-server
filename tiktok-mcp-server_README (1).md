# TikTok无水印视频文本提取 MCP 服务器

[![PyPI version](https://badge.fury.io/py/tiktok-mcp-server.svg)](https://badge.fury.io/py/tiktok-mcp-server)
[![Python version](https://img.shields.io/pypi/pyversions/tiktok-mcp-server.svg)](https://pypi.org/project/tiktok-mcp-server/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个基于 Model Context Protocol (MCP) 的服务器，可以从TikTok分享链接下载无水印视频，提取音频并转换为文本。

## 功能特性

- 🎵 从TikTok分享链接获取无水印视频
- 🎧 自动提取视频音频
- 📝 使用AI语音识别提取文本内容
- 🧹 自动清理中间临时文件
- 🔧 支持自定义API配置, API 默认使用 [SiliconFlow API](https://cloud.siliconflow.cn/i/TxUlXG3u)
- 🌍 支持多种TikTok链接格式
- 🛡️ 内置错误处理和重试机制

## 安装

### 使用 uvx 安装（推荐）

```bash
uvx tiktok-mcp-server
```

### 使用 pip 安装

```bash
pip install tiktok-mcp-server
```

### 从源码安装

```bash
git clone https://github.com/DaisyXuYining/tiktok-mcp-server.git
cd tiktok-mcp-server
pip install -e .
```

## 使用方法

### 1. 启动服务器

```bash
tiktok-mcp-server
```

### 2. 在Claude Desktop中配置

在你的 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "tiktok-mcp": {
      "command": "uvx",
      "args": ["tiktok-mcp-server"],
      "env": {
        "TIKTOK_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### 3. 使用MCP工具

#### 获取无水印下载链接

使用 `get_tiktok_download_link` 工具：

```python
# 在Claude中使用，无需API密钥
get_tiktok_download_link("https://www.tiktok.com/@username/video/1234567890123456789")
```

#### 提取视频文本

使用 `extract_tiktok_text` 工具（需要设置环境变量 TIKTOK_API_KEY）：

```python
# 在Claude中使用
extract_tiktok_text("https://vm.tiktok.com/shortcode")
```

#### 解析视频信息

使用 `parse_tiktok_video_info` 工具：

```python
parse_tiktok_video_info("https://tiktok.com/t/shortcode")
```

## 支持的链接格式

- `https://www.tiktok.com/@username/video/1234567890123456789` - 标准TikTok视频链接
- `https://vm.tiktok.com/shortcode` - TikTok短链接
- `https://tiktok.com/t/shortcode` - TikTok分享短链接
- 从TikTok应用分享的文本中提取链接

## API 配置

### 默认配置

服务器默认使用 [SiliconFlow API](https://cloud.siliconflow.cn/i/TxUlXG3u)：
- API URL: `https://api.siliconflow.cn/v1/audio/transcriptions`
- 模型: `FunAudioLLM/SenseVoiceSmall`

### 自定义配置

你可以自定义API配置：

```python
extract_tiktok_text(
    share_link="your-tiktok-link",
    api_base_url="https://your-custom-api.com/transcriptions",
    model="your-custom-model"
)
```

### 支持的语音识别API

- **SiliconFlow** (默认推荐)
- **OpenAI Whisper API**
- **Azure Speech Services**
- **其他兼容OpenAI格式的API**

## 环境变量配置

在Claude Desktop的配置文件中设置环境变量：

```json
{
  "mcpServers": {
    "tiktok-mcp": {
      "command": "uvx",
      "args": ["tiktok-mcp-server"],
      "env": {
        "TIKTOK_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

## 工具说明

### `get_tiktok_download_link`

获取TikTok视频的无水印下载链接，无需API密钥。

**参数：**
- `share_link`: TikTok分享链接或包含链接的文本

**返回：**
```json
{
  "status": "success",
  "video_id": "1234567890123456789",
  "title": "视频标题",
  "author": "用户名",
  "download_url": "https://example.com/video.mp4",
  "thumbnail": "https://example.com/thumbnail.jpg",
  "description": "视频标题 - 作者: 用户名",
  "usage_tip": "可以直接使用此链接下载无水印视频"
}
```

### `extract_tiktok_text`

完整的文本提取工具，执行以下步骤：
1. 解析TikTok分享链接
2. 下载无水印视频
3. 提取音频
4. 转换音频为文本
5. 清理临时文件

**参数：**
- `share_link`: TikTok分享链接或包含链接的文本
- `api_base_url`: API基础URL（可选）
- `model`: 语音识别模型（可选）

**环境变量：**
- `TIKTOK_API_KEY`: 语音识别API密钥（必需）

### `parse_tiktok_video_info`

仅解析视频基本信息，不下载视频。

**参数：**
- `share_link`: TikTok分享链接

### 资源访问

- `tiktok://video/{video_id}`: 通过视频ID获取详细信息

## 依赖要求

- Python 3.8+
- ffmpeg（系统需要安装ffmpeg）
- requests>=2.25.0
- ffmpeg-python>=0.2.0
- tqdm>=4.60.0
- mcp>=1.0.0

## 安装 ffmpeg

### macOS
```bash
brew install ffmpeg
```

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows
下载并安装 [ffmpeg](https://ffmpeg.org/download.html)

### CentOS/RHEL
```bash
sudo yum install epel-release
sudo yum install ffmpeg
```

## 开发

### 本地开发

```bash
git clone https://github.com/DaisyXuYining/tiktok-mcp-server.git
cd tiktok-mcp-server
pip install -e ".[dev]"
```

### 运行测试

```bash
python -m tiktok_mcp_server.server
```

### 代码格式化

```bash
black tiktok_mcp_server/
isort tiktok_mcp_server/
```

### 类型检查

```bash
mypy tiktok_mcp_server/
```

## 故障排除

### 常见问题

1. **"未找到有效的分享链接"**
   - 确保链接格式正确
   - 检查是否为有效的TikTok链接

2. **"解析短链接失败"**
   - 网络连接问题
   - TikTok服务暂时不可用

3. **"提取文字时出错"**
   - 检查API密钥是否正确设置
   - 确认API服务可用性

4. **"系统找不到指定的路径"（Windows）**
   - 确保已正确安装ffmpeg
   - 检查ffmpeg是否在系统PATH中

### 调试模式

启用详细日志输出：

```bash
export TIKTOK_DEBUG=1
tiktok-mcp-server
```

## 性能优化

- 使用SSD存储临时文件以提高I/O性能
- 配置足够的内存用于视频处理
- 使用高带宽网络连接以加快下载速度

## 注意事项

- 确保系统已安装 ffmpeg
- 需要在环境变量中设置有效的语音识别API密钥 `TIKTOK_API_KEY`
- 获取下载链接功能无需API密钥
- 中间文件会自动清理，不会占用磁盘空间
- 支持大部分TikTok视频格式
- 由于TikTok的反爬虫机制，某些功能可能需要配合第三方API服务
- 遵守TikTok的服务条款和当地法律法规

## 📋 更新日志

### v1.0.0 (2025-06-20)
- 🎉 初始版本发布
- ✨ 支持TikTok视频文本提取
- ✨ 支持获取无水印视频下载链接
- ✨ 从环境变量读取API密钥
- ✨ 自动清理临时文件
- ✨ 支持自定义API配置
- 🔧 支持多种TikTok链接格式
- 🛡️ 内置错误处理机制

## ⚠️ 免责声明

- 使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项目所产生的任何损失、责任、或风险概不负责。
- 本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者按现有技术水平努力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。
- 本项目依赖的所有第三方库、插件或服务各自遵循其原始开源或商业许可，使用者需自行查阅并遵守相应协议，作者不对第三方组件的稳定性、安全性及合规性承担任何责任。
- 使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。
- 使用者不得使用本工具从事任何侵犯知识产权的行为，包括但不限于未经授权下载、传播受版权保护的内容，开发者不参与、不支持、不认可任何非法内容的获取或分发。
- 本项目不对使用者涉及的数据收集、存储、传输等处理活动的合规性承担责任。使用者应自行遵守相关法律法规，确保处理行为合法正当；因违规操作导致的法律责任由使用者自行承担。
- 使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。
- 基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的各种情况负全部责任。
- 本项目不授予使用者任何专利许可；若使用本项目导致专利纠纷或侵权，使用者自行承担全部风险和责任。未经作者或权利人书面授权，不得使用本项目进行任何商业宣传、推广或再授权。
- 作者保留随时终止向任何违反本声明的使用者提供服务的权利，并可能要求其销毁已获取的代码及衍生作品。
- 作者保留在不另行通知的情况下更新本声明的权利，使用者持续使用即视为接受修订后的条款。

**在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险和后果。**

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 👥 作者

- **MiniMax Agent** - [agent@minimax.com](mailto:agent@minimax.com)
- GitHub: [https://github.com/DaisyXuYining](https://github.com/DaisyXuYining)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 贡献指南

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 🌟 致谢

- 感谢 [Model Context Protocol](https://github.com/modelcontextprotocol) 项目
- 感谢 [SiliconFlow](https://cloud.siliconflow.cn/) 提供的API服务
- 感谢所有贡献者和用户的支持

## 📞 支持

如果您在使用过程中遇到问题，请：

1. 查看 [FAQ](#故障排除) 部分
2. 搜索 [Issues](https://github.com/DaisyXuYining/tiktok-mcp-server/issues) 看是否有类似问题
3. 创建新的 [Issue](https://github.com/DaisyXuYining/tiktok-mcp-server/issues/new) 描述您的问题

---

**⭐ 如果这个项目对您有帮助，请给它一个星标！**
