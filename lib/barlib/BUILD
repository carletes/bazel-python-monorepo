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

load("@pip_barlib//:requirements.bzl", requirement = "requirement")

py_library(
    name = "barlib",
    srcs = [
        "__init__.py",
    ],
    deps = [
        requirement("psutil"),
    ],
)

py_image(
    name = "hello",
    srcs = [
        "hello-bar.py",
    ],
    deps = [
        ":barlib",
    ],
    imports = [
        "..",
    ],
    main = "hello-bar.py",
)
