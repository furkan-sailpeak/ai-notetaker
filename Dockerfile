FROM python:3.9-slim

# Install minimal dependencies for Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
COPY meetbot.py .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "meetbot.py"]
COPY meetbot.py .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "meetbot.py"]
