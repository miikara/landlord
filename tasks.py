from invoke import task

# Currently starts app, later a separate ui launcher
@task
def start(ctx):
    ctx.run("python3 src/service.py")

@task
def test(ctx):
    ctx.run("python3 src/service_test.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")