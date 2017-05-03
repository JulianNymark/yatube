FROM nginx

WORKDIR /usr/src/yatube

COPY apt ./apt

# update to unstable + some apt deps
RUN cp apt/sources.list /etc/apt/sources.list \
    && apt update && apt upgrade -y \
    build-essential \
    python3.6-dev \
    python3-pip \
&& rm -rf /var/lib/apt/lists/*

# python deps
RUN python3.6 -m pip install -U sanic jinja2

COPY Makefile .
COPY yatube.py .
# COPY nginx /etc/nginx

CMD ["nginx", "-g", "daemon off;"]
