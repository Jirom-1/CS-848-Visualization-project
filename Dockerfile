FROM python:3.10.8

COPY . .
RUN apt update  -y
RUN apt-get install -y graphviz graphviz-dev
RUN pip3 install -r requirements.txt

ENV PORT=80
EXPOSE 80

# CMD bokeh serve --port=$PORT --num-procs=0 --allow-websocket-origin=cs-848-viz.herokuapp.com --address=0.0.0.0 --use-xheaders app.py
CMD bokeh serve app.py --port=80 --allow-websocket-origin='*' --address=0.0.0.0 --use-xheaders