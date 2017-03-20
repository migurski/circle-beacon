# Circle Beacon

Alerts Circle CI to retry the last successful build on a named branch.
This is useful when Circle is used as part of a deploy pipeline, and
you want to trigger a fresh build from an upstream repository.

Use it like this:

    alert-circle <github owner> <github repo> <branch name> <circle API token>

Previously named Circle Tickler.