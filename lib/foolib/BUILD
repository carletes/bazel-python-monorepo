package(default_visibility = ["//visibility:public"])

load(
    "@io_bazel_rules_python//python:python.bzl",
    "py_binary",
    "py_library",
    "py_test",
)

load(
    "@io_bazel_rules_docker//python:image.bzl",
    "py_image",
)

load("@pip_foolib//:requirements.bzl", "requirement")

py_library(
    name = "foolib",
    srcs = [
        "__init__.py",
    ],
    deps = [
        requirement("requests"),
        "//lib/barlib:barlib",
    ],
)

py_image(
    name = "hello",
    srcs = [
        "hello-foo.py",
    ],
    deps = [
        ":foolib",
    ],
    imports = [
        "..",
    ],
    main = "hello-foo.py",
)
