FROM alpine:3.5

WORKDIR /opt/app

COPY . /opt/app

# Install dependencies
RUN  apk --no-cache add bash python3 \
  && ln -s /usr/bin/python3 /usr/bin/python

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
ENTRYPOINT ["python", "run.py"]
CMD ["run"]
