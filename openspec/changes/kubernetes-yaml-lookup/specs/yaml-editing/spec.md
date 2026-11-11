## ADDED Requirements

### Requirement: Schema completion for manifests
Kubernetes manifests SHALL get completion and validation from the Kubernetes and CRD schemas.

#### Scenario: Unknown field
- **WHEN** a Deployment has a misspelled field
- **THEN** a diagnostic names the field

### Requirement: Component docs in the editor
The docs of the components a project uses SHALL be readable from the editor through `:help`, `K` and a popup.

#### Scenario: Hover an ingress annotation
- **WHEN** the user presses K on an ingress annotation
- **THEN** the component's doc for it shows, without a browser
