FROM alpine:3.5

# Set the working directory to /app
WORKDIR /opt/app

# Copy the current directory contents into the container at /app
COPY . /opt/app

# Install dependencies
RUN apk add --no-cache \
  bash \
  python3 \
  && ln -s /usr/bin/python3 /usr/bin/python

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["gunicorn", "-b :8000", "wsgi:application"]
