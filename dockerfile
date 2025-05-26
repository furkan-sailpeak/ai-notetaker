FROM python:3.9-slim
RUN apt-get update && apt-get install -y chromium-driver
COPY meetbot.py .
RUN pip install flask selenium
CMD ["python", "meetbot.py"]
