---
title: x-archive-visualizer
emoji: 📊
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
license: mit
---

<p align="center">
  <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/x-archive-visualizer/refs/heads/main/docs/x-archive-visualizer.png" width="100%">
  <h1 align="center">🌟 x-archive-visualizer 🌟</h1>
</p>
<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/x-archive-visualizer">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/github-x--archive--visualizer-blue?logo=github">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/x-archive-visualizer/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/Sunwood-ai-labs/x-archive-visualizer?color=green">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/x-archive-visualizer/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/x-archive-visualizer?style=social">
  </a>
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/x-archive-visualizer">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/x-archive-visualizer">
</p>
<h2 align="center">
  ～ Xアーカイブの可視化ツール ～

<a href="https://github.com/Sunwood-ai-labs/x-archive-visualizer/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
</h2>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5" alt="HTML">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript" alt="JavaScript">
  <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3" alt="CSS">
  <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown" alt="Markdown">
</p>

## 🚀 プロジェクト概要

x-archive-visualizerは、Xの動画アーカイブを可視化し、インタラクティブな形式で表示するためのツールです。Streamlitを使用してWebアプリケーションを構築し、HTMLとJavaScriptを組み合わせてダイナミックな表示を実現しています。

## 🆕 主な機能

- Streamlitを使用したWebアプリケーション
- HTMLとJavaScriptを利用した動的な可視化
- Xの活動を時系列で表示
- カテゴリ別の活動サマリー
- インタラクティブなユーザーインターフェース

## 🔧 使用方法

1. リポジトリをクローンします。
2. 必要な依存関係をインストールします：`pip install -r requirements.txt`
3. Streamlitアプリを実行します：`streamlit run app.py`
4. ブラウザでアプリケーションにアクセスします。

## 📦 ファイル構造

- `app.py`: Streamlitアプリケーションのメインファイル
- `demo.html`: 可視化のためのHTMLテンプレート
- `js_to_markdown_converter.py`: JavaScriptファイルからマークダウンへの変換スクリプト
- `README.md`: プロジェクトのドキュメント

## 🌿 環境構築

1. Pythonの仮想環境を作成します：
   ```bash
   python -m venv venv
   ```
2. 仮想環境をアクティベートします：
   ```bash
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. 依存関係をインストールします：
   ```bash
   pip install -r requirements.txt
   ```

## 📚 主要コンポーネント

### 🖥️ Streamlitアプリケーション (`app.py`)
- README.mdファイルの内容を表示
- アプリケーションのメイン画面を提供

### 🎨 可視化テンプレート (`demo.html`)
- Xの活動を視覚的に表示するためのHTMLテンプレート
- JavaScriptを使用したインタラクティブな要素

### 🔄 データ変換スクリプト (`js_to_markdown_converter.py`)
- JavaScriptファイルからマークダウン形式への変換を行う
- ログ機能付きで処理の詳細を記録

## 🤝 コントリビューション

プロジェクトへの貢献を歓迎します。バグ報告、機能リクエスト、プルリクエストなど、あらゆる形での貢献をお待ちしています。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

---

x-archive-visualizerで、あなたのX活動を新しい視点で見てみましょう！
