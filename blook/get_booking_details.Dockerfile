FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN python -m pip install --no-cache-dir -r http.reqs.txt
COPY ./get_booking_details.py ./invokes.py ./
CMD [ "python", "./get_booking_details.py" ]