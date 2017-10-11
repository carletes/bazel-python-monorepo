load(
    "@io_bazel_rules_python//python:python.bzl",
    "py_binary",
    "py_library",
    "py_test",
)

load("@pip_foolib//:requirements.bzl", foolib_requirement = "requirement")

py_library(
    name = "foolib",
    srcs = [
        "__init__.py",
    ],
    deps = [
        foolib_requirement("requests"),
    ],
)

py_binary(
    name = "hello_foo",
    deps = [
        ":foolib",
    ],
    srcs = [
        "hello-foo.py",
    ],
    main = "hello-foo.py",
)
