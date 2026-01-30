FROM python:3.12-slim

WORKDIR /app

# 의존성 명시 설치 (중요)
RUN pip install --no-cache-dir \
    fastapi[standard] \
    uvicorn \
    obs-websocket-py \
    slack-bolt \
    slack-sdk \
    python-dotenv

# 소스 코드
COPY app ./app

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]