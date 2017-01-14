FROM andrewosh/binder-base

MAINTAINER Jessica B. Hamrick <jhamrick@berkeley.edu>

# Install nbgrader
RUN pip install git+git://github.com/jupyter/nbgrader.git

# Install nbgrader extensions
RUN jupyter notebook --generate-config
RUN jupyter nbextension install --sys-prefix --py nbgrader
RUN jupyter nbextension enable --sys-prefix --py nbgrader
RUN jupyter serverextension enable --sys-prefix --py nbgrader

# Setup the exchange directory
USER root
RUN mkdir -p /srv/nbgrader/exchange
RUN chmod ugo+rw /srv/nbgrader/exchange
USER main

# Add the notebook config and formgrade extension
ADD formgrade_extension.py /home/main/formgrade_extension.py
RUN jupyter serverextension enable --sys-prefix formgrade_extension
