# TODO: Install the backend dependency package into the app folder inside the container.
FROM python:3.11
# 設定工作目錄
WORKDIR /app
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
# 開放應用程式的端口
EXPOSE 8000

# 設定環境變數


# 启动应用
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]