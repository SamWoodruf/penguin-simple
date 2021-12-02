FROM tensorflow/tfx:latest
WORKDIR ./pipeline

COPY ./ ./

RUN pip install -r requirements.txt
