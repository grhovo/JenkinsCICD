FROM nginx
RUN apt update && apt -y install python3
WORKDIR /app
COPY . .
RUN python3 -m unittest test_sitecreator.py
RUN python3 sitecreator.py
RUN mv index.html /usr/share/nginx/html

