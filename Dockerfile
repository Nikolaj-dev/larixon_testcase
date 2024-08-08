FROM python:3.12

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

ENTRYPOINT ["sh", "-c", "python manage.py migrate && python create_super_user.py && python manage.py runserver 0.0.0.0:8000"]
