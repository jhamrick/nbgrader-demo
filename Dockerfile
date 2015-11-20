FROM andrewosh/binder-base
MAINTAINER Jessica B. Hamrick <jhamrick@berkeley.edu>

RUN pip install nbgrader
RUN nbgrader extension install --user
RUN nbgrader extension activate
