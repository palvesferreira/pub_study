FROM python:3.13-alpine3.22
EXPOSE 8000

WORKDIR /app/backend
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "9000"]