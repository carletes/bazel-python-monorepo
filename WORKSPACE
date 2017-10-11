workspace(name="bazel_python_monorepo")

# Python support.

git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "c208292d1286e9a0280555187caf66cd3b4f5bed",  # HEAD of `master` as of 2017-10-10
)

load(
    "@io_bazel_rules_python//python:pip.bzl",
    "pip_import",
    "pip_repositories",
)

pip_repositories()

# Import pip dependencies of all our components.

pip_import(
    name = "pip_foolib",
    requirements = "//lib/foolib:requirements.txt",
)
load("@pip_foolib//:requirements.bzl", foolib_pip_install = "pip_install")
foolib_pip_install()