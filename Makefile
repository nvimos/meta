SHELL := pwsh.exe
.SHELLFLAGS := -NoProfile -NoLogo -Command
.DEFAULT_GOAL := help

S ?=

##@ scan

open: ## open tasks by status: in progress, needs test, to do
	python tools/scan.py

review: ## tasks waiting to be tried by hand, with their verify steps
	python tools/scan.py 'Needs Test' --details

doing: ## tasks in progress, with open steps
	python tools/scan.py 'In Progress' --details

status: ## tasks of one status S=..., with details
	python tools/scan.py '$(S)' --details

##@ other

help: ## this list
	@Get-Content $(firstword $(MAKEFILE_LIST)) | Select-String -Pattern '^(##@|[a-z-]+:.*## )' | ForEach-Object { $$l = $$_.Line; if ($$l -like '##@*') { ''; $$l.Substring(4) } else { $$p = $$l -split ':.*## ', 2; '  {0,-8} {1}' -f $$p[0], $$p[1] } }
