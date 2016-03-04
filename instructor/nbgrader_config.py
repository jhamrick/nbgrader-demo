from nbgrader.utils import get_username

c = get_config()

c.NbGrader.course_id = "demo"
c.NbGrader.db_assignments = [dict(name="ps1")]
c.NbGrader.db_students = [dict(id=get_username())]
