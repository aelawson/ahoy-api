
FROM alpine:3.5

WORKDIR /opt/app

COPY . /opt/app

# Install dependencies
RUN apk update \
  && apk add musl-dev gcc bash git postgresql-dev python3 python3-dev \
  && ln -s /usr/bin/python3 /usr/bin/python

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

ENV PYTHONPATH $PYTHONPATH:/opt/app

ENTRYPOINT ["celery"]
CMD ["-A", "celery_app", "worker", "--loglevel=INFO"]
