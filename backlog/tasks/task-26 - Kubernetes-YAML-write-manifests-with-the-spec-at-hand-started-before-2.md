---
id: TASK-26
title: 'Kubernetes YAML: write manifests with the spec at hand, started before 2027, alongside...'
status: To Do
assignee: []
created_date: '2026-11-05'
labels:
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 26000
---

## Description

Kubernetes YAML: write manifests with the spec at hand, started before 2027, alongside...

- test project: ~/es/k8s-minikube-ci in its own WSL distro minikube (AlmaLinux 10; written in alma first, copied by make seed), Windows wrapper C:/Users/jazzo/es/k8s-minikube-ci (Minikube + Tekton CI; phases add git server, ingress, autoscaling;
- the distro is disposable: source, configs and CI state live on the host, synced in (to do in the project)
  each component is one whose docs genja should fetch); nothing run yet, minikube/kubectl/docker not installed
- options while writing a manifest, look things up from inside the editor, no browsing the spec
- values depend on the components in use (router X, ingress Y, autoscaler Z): pull their docs into
  stdpath('data') and show them through familiar interfaces: generated :help files (a help subfolder,
  maybe per project), K hover, or a popup
- today: no yamlls, no schemas (grep: only old/unused specs); lua/genja/ft/yaml.lua maps yml -> yaml.ansible
- ideas: yamlls + schemastore + kubernetes schemas (CRD schemas per component, e.g. datreeio/CRDs-catalog);
  helm/kustomize files; docs fetched per component into stdpath('data'), turned into vim help; check existing plugins first
- more languages found missing (terraform, helm, alloy, promql, sql, toml, systemd, parsers, linters): todo-ideas/grafana-k8s-terraform-langs.md (2026-11-07)

From `todo-ideas.md`, section "ideas october".

## Original notes

```markdown
- [ ] Kubernetes YAML: write manifests with the spec at hand, started before 2027, alongside the LLM chat survey (2026-11-05)
  - test project: ~/es/k8s-minikube-ci in its own WSL distro minikube (AlmaLinux 10; written in alma first, copied by make seed), Windows wrapper C:/Users/jazzo/es/k8s-minikube-ci (Minikube + Tekton CI; phases add git server, ingress, autoscaling;
  - the distro is disposable: source, configs and CI state live on the host, synced in (to do in the project)
    each component is one whose docs genja should fetch); nothing run yet, minikube/kubectl/docker not installed
  - options while writing a manifest, look things up from inside the editor, no browsing the spec
  - values depend on the components in use (router X, ingress Y, autoscaler Z): pull their docs into
    stdpath('data') and show them through familiar interfaces: generated :help files (a help subfolder,
    maybe per project), K hover, or a popup
  - today: no yamlls, no schemas (grep: only old/unused specs); lua/genja/ft/yaml.lua maps yml -> yaml.ansible
  - ideas: yamlls + schemastore + kubernetes schemas (CRD schemas per component, e.g. datreeio/CRDs-catalog);
    helm/kustomize files; docs fetched per component into stdpath('data'), turned into vim help; check existing plugins first
  - more languages found missing (terraform, helm, alloy, promql, sql, toml, systemd, parsers, linters): todo-ideas/grafana-k8s-terraform-langs.md (2026-11-07)
```
