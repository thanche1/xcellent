.PHONY .SILENT: default
default: gomod gofmt golint gotest gobin

# Implement the shown instructions by running them in a golang:1.17 container

.PHONY .SILENT: gomod
gomod:
	#go mod download
	#go mod tidy -compat=1.17

.PHONY .SILENT: gofmt
gofmt:
	#go fmt ./...

.PHONY .SILENT: golint
golint:
	#golangci-lint run -p bugs -p unused

.PHONY .SILENT: gotest
gotest:
	#go test ./...

.PHONY .SILENT: gobin
gobin:
	#go build -o bin/vocabulary-trainer
