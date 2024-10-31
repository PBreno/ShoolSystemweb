FROM python:3.12-slim

WORKDIR /var/www

COPY ../src/public/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "public.main:app", "--host", "0.0.0.0", "--port", "8000"]