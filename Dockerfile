FROM bamos/openface

COPY . /megh

RUN \
  cd /megh && \
  pip install -r requirements.txt

CMD python /megh/app.py
