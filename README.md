# SL-5-1 SRMD Validator

This python code is meant to be used in a CI pipeline, e.g. a GitHub Action.
It looks for SRMD files in the root directory of a repository, this repo is cloned into.
The found SRMD files are validated against the SRMD schema from [SSPTraceability](https://github.com/PMSFIT/SSPTraceability/).
