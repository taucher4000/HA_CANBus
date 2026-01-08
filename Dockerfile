ARG BUILD_FROM
FROM $BUILD_FROM

RUN mkdir /canbus
COPY run.sh /canbus/
RUN chmod a+x /canbus/run.py

# Install dependencies, create venv, upgrade pip, install miqro_can
RUN apk add --no-cache python3 py3-pip git \
    && python3 -m venv /canbus \
    && source canbus/bin/activate \
    && /canbus/bin/pip install --upgrade pip \
    && cd /canbus \
    && git clone https://github.com/danielfett/miqro_can.git \
    && /canbus/bin/pip3 install -r miqro_can/requirements.txt 
   
# Add venv to PATH
ENV PATH="/canbus/bin:$PATH"

CMD [ "/canbus/run.py" ]