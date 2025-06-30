# 軟體測試期末專案 - 第10組《電影時刻 Movie Time》

## 專案概述

本專案針對《電影時刻 Movie Time》App 進行功能性測試，採用黑箱測試與圖形展開的測試技術，以 Edge Coverage 為覆蓋測試模型，確保 App 主要功能表現穩定、順暢。

## 專案組員

| 姓名  | 分工模組                     |
| --- | ------------------------ |
| 雍皓崴 | Scenario 設計、文件撰寫         |
| 康紘郡 | 電視台功能測試實作、文件撰寫           |
| 王少雷 | 電影院功能測試實作、文件撰寫           |
| 吳佳蓉 | 電影功能測試實作、文件撰寫            |
| 王尚鵬 | User Story、Graph 設計、文件撰寫 |

## 測試目標

- 黑箱測試無需原始碼
- 點擊操作與 UI 式測試
- 檢驗功能是否符合用戶預期之作業流程
- 確保功能設計無誤，準備上架

## 測試概測

| 功能模組   | 測試案例數 |
| ------ | ----- |
| 電影院功能  | 5     |
| 電影功能   | 2     |
| 電視節目功能 | 4     |
| 合計     | 11    |

## 環境設定與執行步驟

### 所需環境

- Python 3.8+
- Appium Server
- Android Studio 
- Visual Studio 2022
- Android 16.0 模擬器
- 電影時刻 APK

### 安裝步驟

1. 安裝 Appium 與相關依賴
2. 安裝 Android Studio 以進行模擬
3. 啟動 Android 模擬器並安裝 APK
4. 啟動 Appium Server

### 執行測試

```bash
python test-scripts/test_theater.py        # 電影院功能
python test-scripts/test_movie.py          # 電影功能
點擊執行 test-scripts/test_tv_program/test_tv_program.bat     # 電視節目功能
```

## 測試結果

| 模組     | 測試案例數 | 通過率  |
|  ------- | --------- | ------ |
| 電影院功能   | 5     | 100% |
| 電影功能     | 2     | 100% |
| 電視節目功能 | 4     | 100% |
| 合計         | 11    | 100% |

### 測試結論

- 全數案例都順利通過
- 功能表現合理，系統反應正確
- 無 Bug 發生，完成實測符合上架準則

## 專案簡報內容

期末簡報檔案：`FinalPresentation.pdf`

簡報內容包含：
- 測試方法與策略
- 測試案例設計
- 測試執行結果
- 問題分析與結論

## 專案檔案組織

```
FinalPresentation/
├── README.md                          ← 本說明文件
├── FinalPresentation.pdf              ← 期末簡報
├── test-documents/                    ← 測試相關文件
│   └── TestPlan.pdf
│   
│   
├── source-code/                       ← 受測 APK 或原始碼
│   └── movie-time.apk
├── test-scripts/                      ← 自動化測試腳本
│   ├── test_theater.py
│   ├── test_movie.py
│   ├── requirement.txt
│   └── test_tv_program/
│       ├── MovieTime.robot
│       ├── requirement.txt
│       ├── test_tv_program.bat
│       └── reports/
│           ├──log.html
│           ├──output.xml
│           └──report.html
                       
│   
└── video/                             ← 測試執行影片
    ├── theater_demo.mkv
    ├── movie_demo.mkv
    └── tv_demo.mp4
```

## 測試影片

- 電影院功能：[https://www.youtube.com/watch?v=HuT46jvc8Ng](https://www.youtube.com/watch?v=HuT46jvc8Ng)
- 電影功能：[https://www.youtube.com/watch?v=p5-72Il5nYI](https://www.youtube.com/watch?v=p5-72Il5nYI)
- 電視節目功能：[https://docs.google.com/file/d/1aSZYtM7pSSFk4rM1X4ahf5EwrKodxruQ/preview](https://docs.google.com/file/d/1aSZYtM7pSSFk4rM1X4ahf5EwrKodxruQ/preview)

## Release 建議

本 App 通過全數測試，功能穩定，推薦立即進行上架與系統部署。

