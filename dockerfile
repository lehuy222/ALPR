FROM 7b19919b069b

WORKDIR /home/lehuy/Downloads/TelegramDesktop/my_API

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

Run pip install torch==1.5.1+cu101 torchvision==0.6.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html

RUN pip install python-multipart

RUN pip install lmdb

CMD ["python","main.py"]

