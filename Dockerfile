FROM python:3.10.8

COPY . .
RUN apt update  -y
RUN apt-get install -y graphviz graphviz-dev
RUN pip3 install -r requirements.txt

EXPOSE 5006

CMD ["bokeh", "serve", "--show", "app.py"]