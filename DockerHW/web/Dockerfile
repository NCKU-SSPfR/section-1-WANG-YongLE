
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式
COPY . .

# 開放 Flask 服務的端口
EXPOSE 5000

# 設定環境變數，確保 Flask 在 Docker 環境中正常運行
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONUNBUFFERED=1  

# 啟動 Flask 應用
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]