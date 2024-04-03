FROM python:3.10

RUN pip install ib_insync
RUN pip install pandas

COPY run.py ./

CMD ["python", "run.py"]
