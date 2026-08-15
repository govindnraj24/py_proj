# docker our python for web app

FROM python:3.8
WORKDIR /app
RUN pip install flask
COPY phython_rev/web/templates/ ./templates/
COPY phython_rev/web/app.py .
EXPOSE 5000
CMD ["python", "app.py"]
