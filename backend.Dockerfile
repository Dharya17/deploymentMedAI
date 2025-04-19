# Use a base image that supports Python
FROM python:3.12-slim

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies (curl, wget, etc.)
RUN apt-get update && apt-get install -y \
    curl \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libxrender1 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN curl -sSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh \
    && bash miniconda.sh -b -p /opt/conda \
    && rm miniconda.sh \
    && /opt/conda/bin/conda init bash

# Add Conda to the PATH
ENV PATH="/opt/conda/bin:$PATH"

# Copy environment.yml and create the Conda environment
COPY backend/environment.yml .
RUN conda env create -f environment.yml

# Activate the environment
RUN echo "conda activate medAI" >> ~/.bashrc

# Set default shell to bash to enable conda activation
SHELL ["/bin/bash", "-c"]

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
