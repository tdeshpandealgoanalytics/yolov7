FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04
FROM python:3.8

RUN python -m pip install --upgrade pip
RUN apt-get update -y  
RUN apt-get install -y python3-pip python3-dev libsm6 libxext6 libxrender-dev




RUN \
	apt-get install -y \
	wget \
	unzip \
	ffmpeg \ 
	git 




COPY requirements.txt ./


RUN pip install -r requirements.txt

WORKDIR /app/yolov7-custom
CMD [ "python", "./pythonTrainingScript.py"]








