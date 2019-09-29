# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /write_number_api
WORKDIR /write_number_api

# Copy the current directory contents into the container at /write_number_api
COPY . /write_number_api

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install gunicorn3
RUN sudo apt install gunicorn3

# Run gunicorn3 listening to port 3000
CMD gunicorn3 -b localhost:3000 -w 4 write_number_api:app