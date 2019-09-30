# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /write_number_api
WORKDIR /write_number_api

# Copy the current directory contents into the container at /write_number_api
COPY . /write_number_api

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run flask development server
CMD flask run --host=0.0.0.0