FROM python:3.12-slim

WORKDIR /app

#Copy required files
COPY requirements.txt .
COPY src/ ./src/

#Install dependencies
RUN pip install --upgrade pip
RUN pip install awslambdaric
RUN pip install --no-cache-dir -r requirements.txt

#Make script readable and execuatble
RUN chmod -R a+rX /app

#Command to run your custom application
ENTRYPOINT ["/usr/local/bin/python", "-m", "awslambdaric"]
CMD ["src.lambda_function.lambda_function"]



