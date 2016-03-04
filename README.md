# nbgrader demo

This is a simple demo of a basic nbgrader setup. This demo illustrates the following features of nbgrader:

* creating assignments (instructor)
* releasing assignments (instructor)
* fetching assignments (student)
* submitting assignments (student)
* collecting assignments (instructor)
* autograding assignments (instructor)
* manually grading assignments with the formgrader (instructor)

You can launch the demo using Binder:

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/jhamrick/nbgrader-demo)

The example assignment is located in `instructor/source`. You can edit it to add new problems, change points, etc.

Once you are happy with the assignment, you can open a terminal and run `nbgrader assign` to create the student version of the assignment:

    cd instructor
    nbgrader assign ps1

The student version will be located in `instructor/release`. You can "release" it to students with (still from the `instructor` directory):

    nbgrader release ps1

You should now be able to fetch, edit, and submit assignments from the notebook list, under the "Assignments" tab. Once you have submitted an assignment, you can collect it (from the `instructor` directory) with:

    nbgrader collect ps1

which will place submitted assignments in `instructor/submitted`. To then autograde those assignments, run (from the `instructor` directory):

    nbgrader autograde ps1

This will place the autograded assignments in `instructor/autograded`. At this point, you would run `nbgrader formgrade` to use the formgrader for manual grading and partial credit. In this binder demo, the formgrader is already automatically running, so rather than running `nbgrader formgrade`, go to the following URL:

```
http://app.mybinder.org/[binder-id]/formgrader
```

where you should replace `[binder-id]` with the id of your currently running binder (this will be different every time you run the demo, so you'll just need to look at the URL and see what it currently is).

After grading, you can generate feedback (from the `instructor` directory) with:

    nbgrader feedback ps1

which will create HTML feedback files in `instructor/feedback`.
