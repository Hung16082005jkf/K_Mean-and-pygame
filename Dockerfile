FROM ubuntu

WORKDIR /src 
RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pygame
RUN apt-get -y install python3-sklearn

COPY Kmeans.py ./Kmeans.py
CMD ["","",""]