# Operator Framework K8S helpers and tools

This is a collection of things that people writing charms for K8S are finding
useful, but they are not quite ready to be brought into the Operator Framework
itself.

Based on work initially done by Mark Maglana.

## How to use it

The best way to use it is via the “opslib” mechanism,

    improt ops.lib

    k8s = ops.lib.use("k8s", 0, "chipaca@canonical.com")

The API is still 0 because there are still two things to do:

* [ ] refactor the tests so they are more readable and depend on
      patching the world less

* [ ] pull in @camille-rodriguez's `K8sPvc`, and add tests for it.
