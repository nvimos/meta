---
id: TASK-26
title: 'Kubernetes YAML: write manifests with the spec at hand, started before 2027, alongside...'
status: Needs Test
assignee: []
created_date: '2026-11-05'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
  - todo-2026-neovim011
  - release-v2026
dependencies: []
ordinal: 26000
---

## Description

Kubernetes YAML: write manifests with the spec at hand, started before 2027, alongside...

Change: `openspec/changes/kubernetes-yaml-lookup/`

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
- v2026 release checklist item 8 (was TASK-48): Kubernetes YAML: schemas, component docs as :help / K / popup (next; test project...

## Branch

Built 2026-11-05 and 2026-11-10 on `PR-k8s-yaml (plugin genja-completion011 PR-yaml-lang)` in the config repo (7d651e8 .. c5fb0ac; plugin f50b6aa), not merged yet:
yamlls, yaml-companion, :K8sHelpBuild + gK, kubectl explain via wsl -d minikube, .k8s-version, SchemaStore.nvim.

## Verify

- [ ] the test session in the branch's `todo-test/k8s-yaml.md` (guided, one step per question)
- [ ] merge the branch into the working branch

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
