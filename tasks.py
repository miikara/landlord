from invoke import task

# Currently starts app, later a separate ui launcher
@task
def start(ctx):
    ctx.run('python3 src/service.py')

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")