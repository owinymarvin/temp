FROM 390274594671.dkr.ecr.eu-west-3.amazonaws.com/awsfusionruntime-python311-build:uuid-python311-20240313-203654-21 AS pre-build-stage

# Ensure pip is installed
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    rm get-pip.py
ENV PYTHONBUFFERED=1
ENV PORT 8080
WORKDIR /app
COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD gunicorn todo_project.wsgi:application --bind 0.0.0.0:"${PORT}"
EXPOSE ${PORT}