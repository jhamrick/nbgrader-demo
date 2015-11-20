FROM andrewosh/binder-base

MAINTAINER Jessica B. Hamrick <jhamrick@berkeley.edu>

# Install nbgrader
RUN pip install nbgrader

# Install nbgrader extensions
RUN nbgrader extension install --user
RUN nbgrader extension activate
