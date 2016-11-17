# Overview

Munin is a system monitoring, network monitoring and infrastructure 
monitoring software application. Munin offers monitoring and alerting 
services for servers, switches, applications, and services. It alerts 
the users when things go wrong and alerts them a second time when the 
problem has been resolved.

Munin is a highly flexible and powerful solution used to create graphs
of virtually everything imaginable throughout your network, while
still maintaining an ease of installation and configuration.
This package contains the grapher/gatherer. You will only need one
use to create graphs and HTML pages, suitable for viewing with your
graphical web browser of choice.  It is also able to alert you if any
value is outside of a preset boundary, useful if you want to be
alerted if a filesystem is about to grow full, for instance.  You can
do this by making Munin run an arbitrary command when you need to be
alert it, or make use of the intrinsic Nagios support.  Munin is
written in Perl, and relies heavily on Tobi Oetiker's excellent
RRDtool. 

For more information go to <http://munin-monitoring.org/>.

# Usage

You can deploy the munin service with the following command:

    juju deploy munin

You can then browse to http://ip-address/munin to view the service.

# Relations
 
The munin charm can be related to monitor several exisiting charms.
The munin interface is present on haproxy, mediawiki, memcached, and
mysql charms.

You can add a relation to those charms by:

    juju add-relation munin:munin mysql:munin
    juju add-relation munin:munin haproxy:munin
    juju add-relation munin:munin memcached:munin

# Configuration

There are no configuration options for munin at this time.  Just deploy the
service and you are all set!

# Contact Information

The munin charm was originally written by Clint Byrum <clint@ubuntu.com>

## Munin information

- [Munin website](http://munin-monitoring.org/)
- [Munin FAQ](http://munin-monitoring.org/wiki/faq)
- [Munin tickets](http://munin-monitoring.org/report)
- [Munin documentation](http://munin.readthedocs.org/en/latest/)
- [Munin mailing list archive](http://sourceforge.net/p/munin/mailman/munin-users/)
- Munin IRC is #munin on irc.oftc.net.
