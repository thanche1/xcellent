# Coding Challenge

Write a Golang CLI called `vocabulary-trainer` that implements the proficiency levels of the [Leitner system](https://en.wikipedia.org/wiki/Leitner_system).

1. Complete the Makefile
1. A user may start a new session by running `bin/vocabulary-trainer` in a terminal, which will prompt her to translate random words of a given vocabulary
    1. Support the command-line flags `--from` and `--to` to specify the languages, e.g. `--from greek --to german`
    1. Support the command-line flag `--count` to define the number of current deck words that will be queried in the session (defaults to 10). The review deck words should be randomly mixed in
    1. Track and visualize all wrong translations
1. Provide 30 greek and 30 english words with their corresponding german translations through two YAML files
    1. Embed these vocabulary files into the Golang binary

# Procedure

You have 4 hours to commit your progress on the main branch.  
Although you may be able to further push afterwards we will only check your code within this time range.

Finally, fork a new branch `docs` from `main`, create a pull request and commit code comments on that `docs` branch, which describe your intentions and strategies (no time limit here).

# Note

Don't worry if you won't finish all tasks in time. Prefer quality over quantity.

Happy coding!
