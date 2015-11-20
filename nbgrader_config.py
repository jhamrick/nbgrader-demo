c = get_config()

c.NbGrader.db_url = "postgresql://postgres@postgres/gradebook"
c.NbGrader.course_id = "demo"
c.IncludeHeaderFooter.header = 'source/header.ipynb'
