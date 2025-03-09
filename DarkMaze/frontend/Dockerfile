# TODO: Install the frontend dependency package into the app folder inside the container.
FROM python:3.11

RUN useradd -m appuser
WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
# 開放應用程式的端口
RUN chown -R appuser:appuser /app
USER appuser
COPY src/ /app/src/
EXPOSE 8088
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
