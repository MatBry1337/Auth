# backend/Dockerfile

# Build stage
FROM python:3.12-slim as builder

WORKDIR /app

# Install system build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies to user space
COPY requirements/dev.txt .
RUN pip install --user --no-cache-dir -r dev.txt

# Runtime stage
FROM python:3.12-slim

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Create application user first
RUN useradd -m -d /app backend_user

WORKDIR /app

# Copy Python dependencies to user space
COPY --from=builder --chown=backend_user:backend_user /root/.local /app/.local

# Set up environment
ENV PATH=/app/.local/bin:$PATH \
    PYTHONPATH=/app

# Copy application files
COPY --chown=backend_user:backend_user . .

# Copy and set entrypoint permissions
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN chown -R backend_user:backend_user /app && \
    chmod 755 /entrypoint.sh

USER backend_user

# Environment configuration
ARG ENVIRONMENT=dev

# Entrypoint and command
ENTRYPOINT ["/entrypoint.sh"]

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
