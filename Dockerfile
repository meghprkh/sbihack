FROM bamos/openface

COPY . /megh

RUN \
  cd /megh && \
  pip install -r requirements.txt

CMD cd /megh && python app.py
