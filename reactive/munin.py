import os
import shutil
import subprocess

from charms.reactive import when, when_not, set_state
from charms.layer import apache
from charmhelpers import fetch
from charmhelpers.core.hookenv import (
    open_port,
    status_set,
    config,
    unit_private_ip,
    log,
)


HTPASSWD = "/etc/munin/munin-htpasswd"
HTDOCS = "/var/cache/munin/www/"


def set_password(user, password):
    log('Setting password for user %s' % user, level='INFO')
    log('super secret pass: %s' % password, level='DEBUG')

    if not password or not user:
        return False

    cmd = ['htpasswd']
    if not os.path.isfile(HTPASSWD):
        cmd.append('-c')

    cmd += ['-b', '-B', HTPASSWD, user, password]
    log('command: %s' % ' '.join(cmd))
    subprocess.check_call(cmd)

    shutil.chown(HTPASSWD, 'www-data', 'www-data')
    return True


@when_not('munin.installed')
@when('apache.available')
def install_munin():
    fetch.apt_install(['munin', 'apache2-utils'])

    if not os.path.isfile(os.path.join(HTDOCS, 'index.html')):
        subprocess.check_call(['touch',
                               os.path.join(HTDOCS, 'index.html')])

    open_port(80)
    set_state('munin.installed')


@when('munin.installed')
@when_not('munin.ready')
def setup_munin():
    apache.configure_site('munin.conf', template='site.conf')
    set_state('munin.ready')
    status_set('active',
               'munin available at http://%s/munin/' % unit_private_ip())


@when('config.changed')
@when('munin.ready')
def config_changed():
    cfg = config()
    set_password('munin', cfg['password'])
