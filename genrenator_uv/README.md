# genrenator-uv

This project was created with `uv init genrenator_uv`

This application uses
the cool [Genrenator API](https://binaryjazz.us/genrenator-api/)
to fetch a made-up music genre, and then returns a simple web page
displaying it to the user.

## Get started

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Run `uv sync`

uv will automatically create the virtual environment
for you, and install a project-specific version of Python
(uv does not use system Python by default).

### Run the development server

`uv run serve.py`

**Difference from Rye:** If you navigate to the bottom of `serve.py`, 
you will notice the "traditional" Pythonic construct

```python
if __name__ == "__main__":
    ...
```

By default, `uv` doesn't provide any special way to run Python scripts without it.

`uv` does allow you to specify an entrypoint, so that you can run your project
with just `uv run [script_name]`, without needing the `if __name__ = ...`,
but it doesn't set that up for you. 
You can find more details on how to get 
that to work in [uv's documentation here](https://docs.astral.sh/uv/concepts/projects/#defining-entry-points)

#### For the adventurous

Try setting up an entrypoint by following uv's docs, so you *can*
just run `uv run genrenator`!

### Run the production server

`uv run hypercorn serve:app`

### Run tests

`uv run pytest` will run tests with `pytest`

**Difference from Rye:** `uv` doesn't provide a test command out of the default.
`uv run pytest` doesn't do anything magic — it just runs the pytest that was installed
in the project's virtual environment, in this case with `uv add --dev pytest`.

As such, `uv` doesn't really expect any particular structure for your tests
— so you can do whatever works with `pytest` or another testing framework.

### Format the code

`uv run black .` will format the code with Black

**Difference from Rye:** Similarly, `uv` doesn't ship with its own formatter.
Currently, you have to bring one in yourself (in this case, with `uv add --dev black`),
and then run it manually every time. While this allows more flexibility, it also
requires you to explicitly think about it when setting up the project.
You also need to execute a command that is longer than just `rye fmt`.

But this does mean that you also explicitly install a specific version of Black,
and track it with the rest of the project's dependencies (which you can do
with Rye, but don't have to out of the box).

#### For the adventurous

Is there a way to set up something like `uv run fmt` using 
[uv entrypoints](https://docs.astral.sh/uv/concepts/projects/#defining-entry-points)?

### Lint the code

Again, uv has no built-in linter, even though [Ruff](https://astral.sh/ruff)
is maintained by the same group of people as uv itself!

So, like the above, you can lint the code with Ruff by running

`uv run ruff check`

Once again, uv provides no magic here out of the box. You are just using
uv to run the Ruff you installed yourself (in this project's case, I added it with
`uv add --dev ruff`), and then having to invoke Ruff with the arguments it expects.

The pros and cons are the same as in the Formatting section above. You
get more flexibility, and you have to explicitly get a specific version
of Ruff (instead of using the one Rye supplies out of the box, which
can lag behind the current release). But you also need to remember
to set that up yourself.

#### For the adventurous

Is there a way to set up something like `uv run lint` using
[uv entrypoints](https://docs.astral.sh/uv/concepts/projects/#defining-entry-points)?

## Extra things to try

If you want to play around more, try to create a Docker image
with this application. uv's documentation describes different ways
you can Dockerize the project [here](https://docs.astral.sh/uv/guides/integration/docker/).

**Difference from Rye:** If you tried Rye's Docker documentation, you will
notice that uv's docs here are *a lot* more comprehensive, and cover more scenarios.
That is, in part, because `uv` itself is more flexible and imposes less
expectations on a project's structure than Rye, but also because the `uv`
project almost certainly had more time and resources to invest into this
part of the documentation.

## Questions to consider

`uv` can feel like *a bit* of a departure from some other Python tooling,
but fundamentally, if you've used something like Poetry, it should not feel
too different (except, uh, a lot faster and, in my opinion, more ergonomic).

Unlike Rye, uv has fewer opinions about what a Python project should look like
and what tools it should use. This is a trade-off — you get less out of the 
box, you have to set up more things yourself, but in return you get more
flexibility, and may need less work to adapt an existing project to `uv`'s
workflow than you would with Rye.

If you've tried both Rye and uv, which approach do you prefer? Are
there other trade-offs or advantages of uv that I haven't considered?

