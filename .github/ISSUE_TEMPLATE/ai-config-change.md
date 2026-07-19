---
name: AI Config Change
about: Track changes to AI configuration, policies, or automation
title: '[ai-config] '
labels:
  - ai-config-action-required
body:
  - type: textarea
    id: summary
    attributes:
      label: Summary
      description: Describe the requested AI config change.
    validations:
      required: true
  - type: textarea
    id: manual-steps
    attributes:
      label: Manual steps
      description: List any steps that cannot be automated.
