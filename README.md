# nbgrader demo

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/jhamrick/nbgrader-demo)

## Resources

* [nbgrader Highlights](http://nbgrader.readthedocs.org/en/latest/user_guide/highlights.html)
* [nbgrader Documentation](http://nbgrader.readthedocs.org/en/latest/)
* [SIGCSE 2016 Demo Slides](http://jhamrick.github.io/sigcse-2016-slides/#/)

## Overview

This is a simple demo of a basic setup of nbgrader a server. This demo illustrates the following features of nbgrader:

* creating assignments with the assignment toolbar and `nbgrader assign` (instructor)
* releasing assignments with `nbgrader release` (instructor)
* fetching assignments with the assignment list extension (student)
* submitting assignments with the assignment list extension (student)
* collecting assignments with `nbgrader collect` (instructor)
* autograding assignments with `nbgrader autograde` (instructor)
* manually grading assignments with the formgrader (instructor)

## Running the demo

You can launch the demo using [Binder](http://mybinder.org/), which is a service for running Jupyter notebook servers initialized with a set of notebooks from a give repository. You can launch the demo by clicking on the badge above that says "launch binder".

If you want to use the demo as a base for getting nbgrader running on your own machine, please note that the demo requires the development version of nbgrader, which you can install with:

```
pip install git+git://github.com/jupyter/nbgrader.git
```

(If you are not interested in running the demo locally then you do not need to worry about installing nbgrader.)

## Creating assignments (instructor)

The example assignment is located in `instructor/source`. You can edit it to add new problems, change points, etc.

Once you are happy with the assignment, you can open a terminal by going to the notebook list and clicking the button that says "New" and then choosing "Terminal". From the terminal, change into the `instructor` directory and run `nbgrader assign` to create the student version of the assignment:

    cd instructor
    nbgrader assign ps1

The student version will now be located in `instructor/release`.

## Releasing assignments (instructor)

After creating the release version of the assignment, you can "release" it to students with (still from the `instructor` directory):

    nbgrader release ps1

## Fetching, completing, and submitting assignments (student)

You should now be able to fetch, edit, and submit assignments from the notebook list, under the "Assignments" tab:

1. You should see "ps1" listed as an assignment, and you can download it by clicking the "Fetch" button.
2. You can expand the assignment by clicking on its name, and then on individual parts of the problem. If you click an individual notebook, the notebook will open and you can try editing it.
2. You can click the "Validate" buttons to verify that your solutions are correct.
3. You can click the "Submit" button to submit the assignment.

## Collecting assignments (instructor)

Once students (which in this demo is just you!) have submitted an assignment, you can collect it (from the `instructor` directory) with:

    nbgrader collect ps1

which will place submitted assignments in `instructor/submitted`.

## Grading assignments (instructor)

To then autograde those assignments, run (from the `instructor` directory):

    nbgrader autograde ps1

This will place the autograded assignments in `instructor/autograded`. At this point, you would run `nbgrader formgrade` to use the formgrader for manual grading and partial credit. In this binder demo, the formgrader is already automatically running, so rather than running `nbgrader formgrade`, go to the following URL:

```
https://app.mybinder.org:80/[binder-id]/formgrader
```

where you should replace `[binder-id]` with the id of your currently running binder (this will be different every time you run the demo, so you'll just need to look at the URL and see what it currently is).

## Generating feedback (instructor)

After grading, you can generate feedback (from the `instructor` directory) with:

    nbgrader feedback ps1

which will create HTML feedback files in `instructor/feedback`.
