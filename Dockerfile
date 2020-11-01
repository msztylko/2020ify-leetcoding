FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY solutions/ ./solutions
COPY tests/ ./tests
RUN ls
RUN cd solutions && make
RUN cd ../tests && pytest
