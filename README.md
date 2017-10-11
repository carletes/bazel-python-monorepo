# A sample monorepo of several Python components.

This monorepo shows how to build several Python components (libraries, commands, container images ...) using [Bazel][]

Thie is the file structure:

	bazel-python-monorepo        # The root of the monorepo
	|
	+- WORKSPACE
	|
	+- lib
		|
		+- foolib                # A Python library, called `foolib`
		    |
			+- BUILD
			|
			+- requirements.txt  # Python dependencies from PyPI
			|
			+- __init__.py       # Library implementation.
			|
			+- hello-foo.py      # A command-line tool, which uses `foolib`


[Bazel]: https://www.bazel.build/
