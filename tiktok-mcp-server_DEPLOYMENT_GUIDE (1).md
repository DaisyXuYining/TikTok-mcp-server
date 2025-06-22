# TikTok MCP Server 部署指南

## 📋 项目概述

您的TikTok MCP服务器已经成功创建！这是一个基于抖音MCP服务器改造的完整TikTok版本，具有以下特性：

- ✅ 从TikTok分享链接获取无水印视频
- ✅ 自动提取视频音频并转换为文本
- ✅ 支持多种TikTok链接格式
- ✅ 内置错误处理和重试机制
- ✅ 支持自定义语音识别API配置
- ✅ 自动清理临时文件

## 🚀 部署到DaisyXuYining的GitHub

### 步骤1：创建GitHub仓库

1. 登录到 DaisyXuYining 的GitHub账户
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 仓库名称设置为：`tiktok-mcp-server`
4. 描述设置为：`TikTok无水印视频文本提取 MCP 服务器`
5. 选择 "Public" 或 "Private"（推荐Public）
6. 不要初始化README、.gitignore或LICENSE（我们已经有了）
7. 点击 "Create repository"

### 步骤2：上传代码

在GitHub创建仓库后，您会看到类似以下的命令，在项目目录中执行：

```bash
# 进入项目目录
cd /workspace/tiktok-mcp-server

# 添加远程仓库（替换为实际的仓库URL）
git remote add origin https://github.com/DaisyXuYining/tiktok-mcp-server.git

# 推送代码到GitHub
git branch -M main
git push -u origin main
```

### 步骤3：配置仓库设置

1. 进入仓库的 Settings 页面
2. 在 "About" 部分添加描述和标签
3. 可以添加以下标签：`tiktok`, `mcp`, `video-download`, `text-extraction`, `python`

## 📦 发布到PyPI（可选）

如果您希望将包发布到PyPI，可以按照以下步骤：

### 准备发布

1. 确保版本号在 `pyproject.toml` 中正确设置
2. 安装构建工具：
   ```bash
   pip install build twine
   ```

3. 构建包：
   ```bash
   cd /workspace/tiktok-mcp-server
   python -m build
   ```

4. 上传到PyPI：
   ```bash
   twine upload dist/*
   ```

## 🔧 本地开发设置

其他开发者可以通过以下方式设置开发环境：

```bash
# 克隆仓库
git clone https://github.com/DaisyXuYining/tiktok-mcp-server.git
cd tiktok-mcp-server

# 安装开发依赖
pip install -e ".[dev]"

# 或使用uv
uv sync --dev
```

## 🧪 测试安装

验证包是否正确安装：

```bash
# 测试导入
python -c "from tiktok_mcp_server import main; print('安装成功！')"

# 运行服务器（测试模式）
tiktok-mcp-server --help
```

## 📝 使用说明

### 在Claude Desktop中配置

在 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "tiktok-mcp": {
      "command": "uvx",
      "args": ["tiktok-mcp-server"],
      "env": {
        "TIKTOK_API_KEY": "your-siliconflow-api-key-here"
      }
    }
  }
}
```

### 支持的功能

1. **获取下载链接**（无需API密钥）：
   ```python
   get_tiktok_download_link("https://www.tiktok.com/@username/video/123")
   ```

2. **提取视频文本**（需要API密钥）：
   ```python
   extract_tiktok_text("https://vm.tiktok.com/shortcode")
   ```

3. **解析视频信息**：
   ```python
   parse_tiktok_video_info("https://tiktok.com/t/shortcode")
   ```

## 🔍 项目结构

```
tiktok-mcp-server/
├── tiktok_mcp_server/           # 主要代码目录
│   ├── __init__.py              # 包初始化文件
│   └── server.py                # MCP服务器实现
├── pyproject.toml               # 项目配置文件
├── README.md                    # 项目说明文档
├── LICENSE                      # MIT许可证
├── .gitignore                   # Git忽略文件
└── DEPLOYMENT_GUIDE.md          # 本部署指南
```

## ⚠️ 注意事项

1. **API密钥**：需要在环境变量中设置 `TIKTOK_API_KEY`
2. **依赖要求**：需要Python 3.10+和ffmpeg
3. **TikTok限制**：由于TikTok的反爬虫机制，某些功能可能需要配合第三方API
4. **合规使用**：请确保使用时遵守相关法律法规和平台条款

## 🆚 与原抖音版本的区别

| 功能 | 抖音MCP | TikTok MCP |
|------|---------|------------|
| 支持平台 | 抖音 | TikTok |
| 链接格式 | 抖音短链接 | TikTok各种格式 |
| API调用 | 抖音API | TikTok/第三方API |
| 错误处理 | 基础 | 增强型 |
| 国际化 | 中文 | 英文+中文 |

## 🎉 完成状态

- ✅ 代码转换完成
- ✅ 功能测试通过
- ✅ 文档编写完成
- ✅ Git仓库初始化
- ⏳ 等待上传到GitHub
- ⏳ 等待发布到PyPI（可选）

---

**项目已准备就绪！请按照上述步骤将代码上传到DaisyXuYining的GitHub账户。**
