# Rollcall System

Rollcall 是一個基於 MySQL 和 FastAPI 的學生出勤管理系統。此系統允許教師和學生查看及更新出勤記錄，並提供相關數據的管理功能。該系統可用于學校或其他機構以管理課程出勤情況。

## 目錄
- [介紹](#介紹)
- [技術棧](#技術棧)
- [安裝與運行](#安裝與運行)
- [功能說明](#功能說明)
- [API 文檔](#api-文檔)
- [資料庫備份與還原](#資料庫備份與還原)
- [授權](#授權)

## 介紹

Rollcall 系統提供了以下基本功能：
- 學生登錄及出勤記錄查看
- 教師能夠查看、更新學生的出勤紀錄
- 依課程、日期範圍等條件篩選出勤紀錄

此系統的後端基於 **FastAPI** 開發，前端可以是任何需要與API交互的應用，無論是Web端還是移動端。

## 技術棧

- **後端**：FastAPI (Python)
- **資料庫**：MySQL
- **ORM**：SQLAlchemy
- **認證方式**：JWT (JSON Web Token)

## 安裝與運行

### 1. 克隆專案

```bash
git clone https://github.com/Mirai1129/Object-Oriented-Software-Engineering.git
```

### 2. 安裝依賴
使用 pip 安裝 Python 依賴：

```bash
pip install -r requirements.txt
```

### 3. 配置資料庫
   請確保你的 MySQL 資料庫已經安裝並運行。可以創建一個新的資料庫來存儲 Rollcall 系統的數據：

```sql
CREATE DATABASE rollcall;
```

### 4. 設置環境變數
   設置資料庫配置和密鑰等環境變數。你可以在 `.env` 文件中配置以下變數：

```ini
USERNAME=your database username
PASSWORD=your database password
HOST=your database host
PORT=your database port
ROLLCALL_DATABASE=Rollcall
PARTICIPATION_DATABASE=Participation
```

### 5. 啟動 FastAPI 服務
   啟動 FastAPI 服務，默認會運行在 http://127.0.0.1:8000：

```bash
uvicorn main:app --reload
```
