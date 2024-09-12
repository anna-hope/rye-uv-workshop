# genrenator-rye

This project was created with `rye init --script genrenator-rye`

This application uses 
the cool [Genrenator API](https://binaryjazz.us/genrenator-api/)
to fetch a made-up music genre, and then returns a simple web page
displaying it to the user.

## Get started

- Install [Rye](https://rye.astral.sh/)
- Run `rye sync`

Rye will automatically create the virtual environment
for you, and install a project-specific version of Python
(Rye does not use system Python by default).

### Run the development server

After running `rye sync`,
`genrenator_rye` (i.e. this project) will be installed into the
virtual environment. So you can simply run it like this:

`rye run genrenator-rye`

Note the `[project.scripts]` section in `pyproject.toml`. That's what tells
Rye what Python code to execute when you run the above command. This 
`[project.scripts]` section in `pyproject.toml` was created by Rye automatically
when I ran `rye init --script genrenator_rye`.

#### Alternative way

You can also run the development server with

`rye run devserver`

Rye knows what to execute here because I manually added a `[tool.rye.scripts]`
section with an entry for `devserver`. The actual result isn't different
in the case of this project, but it can be useful if you want to
provide certain CLI flags or configuration values, so that you don't have to supply them
manually every time.

The Rye documentation explains this section of the `pyproject.toml` [here](https://rye.astral.sh/guide/pyproject/#toolryescripts).

### Run "production" server

You may have a different server configured for production use. In the case
of this project, you can run it with

`rye run prodserver`

Similar to the `devserver`, the above works because I added a `prodserver` entry
to `[tool.rye.scripts]`.

### Run tests

`rye test`

This will run pytest on the files in the `tests` directory, which is where 
Rye expects them to be by default. The `rye test` command is explained in 
more detail in [Rye docs here](https://rye.astral.sh/guide/commands/test/).

### Format the code

`rye fmt` will format the code with Black

### Lint the code

`rye lint` will format the code with Ruff


## Questions to consider

This workflow can feel quite different from the "traditional" Python project
tooling. Rye is obviously more opinionated about the project structure,
and the formatting, linting, and testing tools it uses. You get a lot
out of the box, but you may have to adapt your workflows to fit them.

Do you think there are advantages to Rye being opinionated? Do you like it?

## Extra things to try

If you want to play around more, try to create a Docker image
with this application. The starting point is here, but note that you may need
to make adaptations (that section of Rye's docs could use some more work!):
https://rye.astral.sh/guide/docker/


## Notes

This project was created to give interested Recurse Center folks a chance
to play around with Rye. It's not meant to be a serious application :)
