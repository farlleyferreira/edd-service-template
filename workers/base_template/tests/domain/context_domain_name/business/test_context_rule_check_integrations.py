from source.domain.context_domain_name.business.context_rule_check_integrations import (
    CheckIntegrations,
)


def test_worker_function():
    assert CheckIntegrations().worker_function(1) == None
