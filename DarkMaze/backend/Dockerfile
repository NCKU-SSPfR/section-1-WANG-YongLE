# TODO: Install the backend dependency package into the app folder inside the container.
FROM python:3.11
# 設定工作目錄
WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
# 開放應用程式的端口
EXPOSE 8000

# 設定環境變數
ENV SONAR_TOKEN="sqp_33c87732d0872da2fd809aec49b3d630962cfc99"

# 啟動應用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# End of Selection