FROM python3.14

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install --no-chache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000