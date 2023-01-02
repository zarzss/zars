FROM vckyouubitch/geez:master

RUN git clone -b master https://github.com/izzy-adeeva/RAM-UBOT home/master/ 
   
WORKDIR /home/master/

CMD ["python3", "-m", "rams"]
