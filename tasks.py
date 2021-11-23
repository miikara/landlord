from invoke import task

# Currently starts app, later a separate ui launcher
@task
def start(ctx):
    ctx.run('python3 src/service.py')

@task
def test(ctx):
    ctx.run("pytest src")