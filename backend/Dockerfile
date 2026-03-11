# Gunakan bahasa Python versi 3.9
FROM python:3.9

# Buat folder kerja di dalam server Hugging Face
WORKDIR /code

# Salin daftar library dan install
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Salin seluruh folder aplikasi Anda
COPY ./app /code/app

# PENTING: Hugging Face HANYA membuka port 7860
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]