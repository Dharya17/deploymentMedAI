FROM continuumio/miniconda3

# Set work directory
WORKDIR /app

# Copy environment and create conda env
COPY backend/environment.yml .
RUN conda env create -f environment.yml

# Activate environment
SHELL ["conda", "run", "-n", "medai-env", "/bin/bash", "-c"]

# Copy source code
COPY backend/ .

# Set FastAPI to run on container start
CMD ["conda", "run", "--no-capture-output", "-n", "medai-env", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]