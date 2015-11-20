FROM andrewosh/binder-base

MAINTAINER Jessica B. Hamrick <jhamrick@berkeley.edu>

# Install psychopg2
RUN apt-get -y install libpq-dev
RUN pip install psycopg2

# Install nbgrader
RUN pip install nbgrader

# Install nbgrader extensions
RUN nbgrader extension install --user
RUN nbgrader extension activate
