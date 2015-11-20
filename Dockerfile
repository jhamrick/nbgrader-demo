FROM andrewosh/binder-base
MAINTAINER Jessica B. Hamrick <jhamrick@berkeley.edu>

RUN pip install nbgrader

ADD nbgrader_config.py /home/main/nbgrader_config.py
