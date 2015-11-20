FROM andrewosh/binder-base

MAINTAINER Jessica B. Hamrick <jhamrick@berkeley.edu>

# Install nbgrader
RUN pip install nbgrader

# Install nbgrader extensions
RUN nbgrader extension install --user
RUN nbgrader extension activate

# Setup the exchange directory
USER root
RUN mkdir -p /srv/nbgrader/exchange
RUN chmod ugo+rw /srv/nbgrader/exchange
USER main

# Add the notebook config
ADD jupyter_notebook_config.json /home/main/.jupyter/jupyter_notebook_config.json
