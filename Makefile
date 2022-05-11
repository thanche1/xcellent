.PHONY .SILENT: default
default: build

.PHONY .SILENT: test
test:
	#run unit tests here
	#Bonus: run the tests within a python3 container

.PHONY .SILENT: run
run:
	python3 vocabulary-trainer.py
	#Bonus: run the vocabulary trainer within a python3 container
