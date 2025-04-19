FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Copy environment file and install dependencies
COPY frontend/environment.yml .
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "frontend-env", "/bin/bash", "-c"]

# Copy app code
COPY frontend/ .

# Expose the Streamlit port
EXPOSE 8501

# Entry point
CMD ["conda", "run", "--no-capture-output", "-n", "frontend-env", "streamlit", "run", "MedAI.py"]
