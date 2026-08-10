# 🧬 AI4Bio 智能体 · 生物信息学专业

> 10 个开箱即用的生物信息学 AI 智能体：文献、序列、结构、测序、富集、设计与分析。

```bash
git clone https://github.com/qgeng1465/ai4bio-agents.git
cd ai4bio-agents
python install.py            # 安装全部到全局 agents 目录
```

## ✨ 特性

- ✅ **零配置**：每个智能体是单个 Markdown 文件，含完整专业工作流
- ✅ **即装即用**：`python install.py` 一键装到 AI 助手的全局 agents 目录，任意项目都能 `@调用`
- ✅ **AI4Bio 专业**：PubMed 文献 / NCBI 下载 / BLAST / 序列分析 / 蛋白质结构 / FASTQ 质控 / 富集分析 / 进化树 / CRISPR / 抗体
- ✅ **跨平台**：Windows / macOS / Linux 通用
- ✅ **原创实现**：全部智能体为本项目独立编写

## 🚀 快速开始

### 前置条件
- 已安装支持 Markdown 智能体（agents）的 AI 编程助手
- 已安装 Python 3.9+（用于安装器）

### 安装

```bash
git clone https://github.com/qgeng1465/ai4bio-agents.git
cd ai4bio-agents
python install.py            # 安装全部 10 个
python install.py --list     # 先看有哪些
```

### 使用

在你的 AI 编程助手会话中直接输入：

```
@antibody-analysis 抗体序列分析…
@blast-search 对 DNA 或蛋白序列做 NCBI BLAST 同源搜索，返回 top hits（accession/物种/E值/一致性/描述）。用法…
@crispr-design sgRNA 设计…
```

也可以手动安装：把 `agents/*.md` 复制到你所用的 AI 助手全局 agents 目录
（`install.py` 会自动定位该目录，无需手动查找）。

## 📦 智能体列表（10 个）

| 智能体 | 能力 |
|-------|------|
| `@antibody-analysis` | 抗体序列分析：解析重/轻链，识别框架区与 CDR（IMGT 风格编号）、评估人源化程度与特异性线索。用法：给我抗体序列。 |
| `@blast-search` | 对 DNA 或蛋白序列做 NCBI BLAST 同源搜索，返回 top hits（accession/物种/E值/一致性/描述）。用法：粘贴一段序列或序列文件路径。 |
| `@crispr-design` | sgRNA 设计：在靶序列上扫描 PAM(NGG)、提取 20bp spacer、评估 GC/脱靶并输出候选表。用法：给我靶基因序列或基因名。 |
| `@fastq-qc` | 测序数据质控：分析 FASTQ 文件（reads 数、长度、碱基质量、GC 含量、接头污染），给出过滤建议。用法：给我 FASTQ 文件路径。 |
| `@go-kegg-enrichment` | 基因功能富集分析：用 g:Profiler 对基因列表做 GO / KEGG / 通路富集，输出显著项表格与生物学解读。用法：给我基因符号/ID 列表。 |
| `@ncbi-genbank-download` | 从 NCBI 下载基因/蛋白序列（GenBank、FASTA、gene、protein、nucleotide 等数据库），支持 accession 号、gene symbol 或关键词。用法：给我基因名或序列号。 |
| `@phylogeny-tree` | 构建系统发育树：比对同源序列（MAFFT）→ 建树（邻接法/IQ-TREE）→ 输出 Newick 并解读。用法：给我物种列表或序列文件。 |
| `@protein-structure-pdb` | 蛋白质结构分析：按 PDB ID 拉取结构并总结分辨率、链/残基、配体、功能位点、相关文献；也可分析本地 PDB 文件。用法：给我 PDB ID。 |
| `@pubmed-research` | 检索 PubMed 文献并结构化总结研究主题（标题/作者/期刊/方法/结论/DOI），适合写综述、开题、课题调研。用法：告诉我要检索的主题。 |
| `@sequence-analysis` | 本地序列分析：GC 含量、ORF 查找、翻译、反向互补、长度统计。支持 DNA/RNA/蛋白序列或 FASTA 文件。用法：粘贴序列或给出文件路径。 |

## 🔧 定制智能体服务

需要**专属定制**的智能体？可以把需求发到我邮箱或评论区，支持按你的课题、行业、业务定制。本项目会持续更新更多智能体。

> **其他领域智能体**：⚗️ [AI4Chem 化学](https://github.com/qgeng1465/ai4chem-agents) · 🔬 [AI4科研 科研日常](https://github.com/qgeng1465/ai4research-agents) · 🌱 [日常生活](https://github.com/qgeng1465/daily-agents)

## ⚠️ 免责声明

本仓库提供的智能体**仅用于学习研究及个人合理使用**。
- 智能体分析结果仅供辅助参考，结合专业工具与原始数据复核。
- 各智能体的输出不保证完全准确，请结合专业知识与原始数据复核。
- 请遵守您所在国家/地区的法律法规、各平台服务条款及学术规范，尊重版权与隐私。
- 使用本项目产生的任何风险与法律责任由使用者自行承担。

## ☕ 支持作者

如果这些智能体帮到了你，欢迎扫码赞赏支持，让我有动力持续更新～

<img src="assets/donate.png" alt="赞赏码" width="200">

## 📄 License

[MIT](./LICENSE) © 2026 qgeng1465
