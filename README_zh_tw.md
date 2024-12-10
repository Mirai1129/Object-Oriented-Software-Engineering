# 物件導向軟體工程課程專案：互動式課堂管理系統

## 專案概覽

此專案是作為物件導向軟體工程課程開發的綜合課堂管理系統。系統由兩個主要子系統組成：

1. 點名系統：用於監控學生課堂出席的數位追蹤解決方案。
2. 問答系統：互動式課堂參與平台，允許教師提問、記錄學生回應並追蹤參與分數。

## 主要功能

### 點名系統

* 數位出席追蹤
* 實時學生簽到
* 出席記錄管理
* 詳細出席報告

### 問答系統

* 課堂互動提問
* 回應追蹤
* 參與分數記錄
* 績效分析

### 技術棧

* 後端框架：FastAPI
* 資料庫：MySQL
* ORM：SQLAlchemy
* 身份驗證：JWT（JSON Web Token）
* 密碼管理：Passlib（bcrypt）
* 環境配置：Python-dotenv

### 系統架構

專案遵循物件導向設計原則，將功能劃分為不同模組：

* 使用者管理
* 身份驗證
* 出席追蹤
* 課堂參與
* 成績和報告

## 安裝與設置

### 先決條件

* Python 3.8+
* MySQL
* pip（Python 套件管理器）

### 資料庫初始化
專案根目錄包含 `init.sql` 腳本用於資料庫設置。

### 環境配置
建立 `.env` 文件，包含以下配置：

```bash
# 資料庫設置
USERNAME=root
PASSWORD=0000
HOST=mysql
PORT=3311
ROLLCALL_DATABASE=Rollcall
PARTICIPATION_DATABASE=Participation

# 密鑰
ROLLCALL_SECRET=RollcallCoolSecret
PARTICIPATION_SECRET=ParticipationCoolSecret
```

### 安裝步驟

1. 克隆倉庫

```bash
git clone https://github.com/Mirai1129/Object-Oriented-Software-Engineering.git
cd Object-Oriented-Software-Engineering
```

2. 安裝依賴

```bash
pip install -r requirements.txt
```

3. 初始化資料庫

```bash
# 使用提供的 init.sql 腳本
mysql -u root -p < init.sql
```

4. 啟動應用程式

```bash
uvicorn main:app --reload
```

## API 文檔

### 通過 Swagger UI 探索 API 端點：
`http://127.0.0.1:8000/docs`
