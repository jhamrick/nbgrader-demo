FROM andrewosh/binder-base

MAINTAINER Jessica B. Hamrick <jhamrick@berkeley.edu>

# Install psychopg2
USER root
RUN apt-get update && apt-get -y install libpq-dev && apt-get clean
USER main
RUN pip install psycopg2

# Install nbgrader
RUN pip install nbgrader

# Install nbgrader extensions
RUN nbgrader extension install --user
RUN nbgrader extension activate
