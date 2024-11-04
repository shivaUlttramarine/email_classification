# Use an official Python runtime as a parent image
FROM condaforge/miniforge3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the Conda environment specification
COPY requirements.yml /app/

# Install any needed packages specified in requirements.yml
RUN conda env create -f requirements.yml

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV PATH=/opt/conda/envs/env_email/bin:$PATH 

# Run the application using the conda environment
CMD ["conda", "run", "--no-capture-output", "-n", "env_email", "flask", "run", "--host=0.0.0.0"]
 