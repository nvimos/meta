# Kubernetes YAML with the spec at hand

Status: Needs Test (backlog TASK-26)

## Why

Writing Kubernetes manifests means browsing the spec and each component's docs in a browser. The
values depend on the components in use (router, ingress, autoscaler), so a generic schema isn't enough.

## What Changes

- yamlls with schemastore and Kubernetes schemas, CRD schemas per component (datreeio/CRDs-catalog)
- docs of the components a project uses, fetched into `stdpath('data')` and turned into `:help` files,
  shown through `K` hover and a popup
- helm and kustomize files recognized

## Impact

- `lua/genja/ft/yaml.lua` (today maps yml to yaml.ansible), the yaml lang module, a docs fetcher
- test project `~/es/k8s-minikube-ci` in the WSL distro `minikube`
- more missing languages: `backlog/docs/doc-2 - grafana-k8s-terraform-langs.md`
