## Beyond requirements.txt: Rye and UV

Python is a great language, it has an amazing ecosystem, but dependency management for any non-trivial project 
can be very hard (and they almost all turn out to be non-trivial).

But there are newer tools like [Rye](https://rye.astral.sh/) 
and [uv](https://docs.astral.sh/uv/) that promise to make it easy.

*I know,* we already have the zoo of pip *(one to find them),* 
Poetry *(one to bring them all),* 
Anaconda *(in the darkness bind them),* 
and whatever else, and the last thing we need is yet more ways to manage Python dependencies. 
But Rye and uv might finally be the one to *rule them all.*
Or, uh, you know, just make things better and let you and your collaborators work on the interesting things in your code,
instead of fighting with dependencies and other tooling.

## So what is this?

This repository has two projects. They have functionally the same Python
code, but one was set up with Rye, and the other with uv.

If you want to get hands-on experience with both, and see how much
faster you can get going with a Python project than with most other tooling,
please try them out for yourself! Each project contains its own README
with more instructions.

You can try either one, or both (or none!), but I wrote each README with
the assumption that you'd try the Rye project first, and the uv second.
The main consequence is that in the uv project's README, I call out differences
with Rye, assuming you might have already tried it.

## Extra things to think about

If you've tried the above projects, do you prefer either of their workflows to
one another? Do you prefer either of them to what you might already be used 
to when working with Python projects?

Take a look at each project's `pyproject.toml`. Do you notice any quirks
or differences in either of them? 

`pyproject.toml` is the [current standard](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
for Python tooling broadly, not just uv or Rye. But you might notice that uv and Rye
add their own sections that *aren't* part of the standard 
(notably, `tool.x.dev-dependencies` and the line). Those are definitely useful, and the
standard specification currently provides no alternative. Do you think there might be any issues 
with these tools introducing their own, non-standard structure?


### For the adventurous

The projects in this repository are fairly straightforward. They do
have a number of dependencies, but the project structure itself
isn't that complex.

Both Rye and `uv` really shine when you can use them to maintain
a project over time — upgrading dependencies, onboarding new collaborators,
adapting to new versions of Python, etc. 

So, if you want to try more complex things...

- Try setting up your own project with uv or Rye. Maybe something with 
more complex dependencies like `numpy`, `polars`, `pandas`, or `pytorch` and
`tensorflow`, if you're into those things. Was it more difficult than using `pip`
or `conda`? Is there anything that Rye or uv did that made it less painful? *More painful?*

- Try adapting an existing Python project (maybe on of your own, or 
a project you like, say ... [Blaggregator](https://github.com/recursecenter/blaggregator))
to use either Rye or uv. 

If you do any of the above, let me know how it goes. How was the experience? What were the
rough parts? Did you encounter any particular quirks of either Rye or uv in the process?

#### Links to documentation to help
- [Rye](https://rye.astral.sh/guide/)
- [uv](https://docs.astral.sh/uv/)

## Acknowledgments

Thanks to all the RC folks who attended my somewhat chaotic workshop about these tools!
And also thanks to the creators of Rye and uv for doing so much work to push Python
project management tooling forward. And, finally, thank you to
the creators and maintainers of the [Genrenator API](https://binaryjazz.us/genrenator-api/)
to all

