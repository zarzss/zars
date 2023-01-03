FROM vckyouubitch/geez:master

RUN git clone -b master https://github.com/izzy-adeeva/RAM-UTOD home/master/ 
   
WORKDIR /home/master/

CMD ["python3", "-m", "rams"]
