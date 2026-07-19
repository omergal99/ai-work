Versioning: semantic versioning for .ai (vMAJOR.MINOR.PATCH)
Canary rollout: tag release with canary, deploy to 1-3 repos for 7 days
Monitoring: watch hallucination_rate, eval_pass_rate, token_cost
Rollback: revert tag and re-deploy previous config; open incident and notify maintainers
Signing: all releases must be GPG signed
