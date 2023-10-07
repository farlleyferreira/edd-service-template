from source.domain.context_domain_name.business.context_rule_check_integrations import (
    CheckIntegrations,
)


def test_integrations_status():
    assert CheckIntegrations().integrations_status() == True
