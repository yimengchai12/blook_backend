FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN python -m pip install --no-cache-dir -r http.reqs.txt
COPY ./exchange_coupon.py ./invokes.py ./
CMD [ "python", "./exchange_coupon.py" ]