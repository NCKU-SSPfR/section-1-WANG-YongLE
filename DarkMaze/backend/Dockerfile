# 此 Dockerfile 用於構建一個 Python 3.11 的容器，並安裝後端依賴包。
FROM python:3.11

RUN useradd -m appuser
WORKDIR /app

COPY requirements.txt .

# 安裝 requirements.txt 中列出的所有依賴包，並不使用緩存
RUN pip install --no-cache-dir -r requirements.txt
# 將當前目錄的所有文件複製到容器的 /app 目錄
RUN chown -R appuser:appuser /app
USER appuser
COPY src/ /app/src

EXPOSE 8000

# 設定環境變數（此處可根據需要添加環境變數）

# 启动应用，使用 uvicorn 啟動 FastAPI 應用
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]