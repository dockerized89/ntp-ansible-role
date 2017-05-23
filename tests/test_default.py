import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ntp_package(Package):
    ntp = Package("ntp")
    ntpd = Package("ntpd")
    assert ntp.is_installed or ntpd.is_installed


def test_ntp_service(Service):
    ntp = Service("ntp")
    ntpd = Service("ntpd")
    assert ntp.is_running or ntpd.is_running
