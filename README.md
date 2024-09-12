## Beyond requirements.txt: Rye and UV

Python is a great language, it has an amazing ecosystem, but dependency management for any non-trivial project 
can be very hard (and they almost all turn out to be non-trivial).

But there are newer tools like [Rye](https://rye.astral.sh/) 
and [uv](https://docs.astral.sh/uv/) that promise to make it easy.

*I know,* we already have the zoo of pip *(one to find them),* 
Poetry *(one to bring them all),* 
Anaconda *(in the darkness bind them),* 
and whatever else, and the last thing we need is yet more ways to manage Python dependencies. 
But Rye and uv might finally be the one to rule them all.

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

### For the adventurous

The projects in this repository are fairly straightforward. They do
have a number of dependencies, but the project structure itself
isn't that complex.

Both Rye and `uv` really shine when you can use them to maintain
a project over time — upgrading dependencies, onboarding new collaborators,
adapting to new versions of Python, etc. 

So, if you want to try more complex things...

Try adapting an existing Python project (maybe on of your own, or 
a project you like, say ... [Blaggregator](https://github.com/recursecenter/blaggregator))
to use either Rye or uv. 

If you do, let me know how it goes. How was the experience? What were the
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

