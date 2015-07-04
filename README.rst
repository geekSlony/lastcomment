Last Comment
============

Last Comment is a small script to query OpenStack's gerrit server
and print the most recent comments by a user. Where the user can be a human
or a CI system.

Dependencies
------------

`requests`

Help
-----

    ./lastcomment.py -h

Usage
-----

To see the last time the user 'Third Party CI'  commented anywhere

    ./lastcomment.py -n 'Third Party CI'

To print the last 30 comments by 'Third Party CI' on the repo openstack/cinder

    ./lastcomment.py -n 'Third Party CI' -m -p openstack/cinder


To print the last 30 votes by 'Third Party CI' on the repo openstack/cinder

    ./lastcomment.py -n 'Third Party CI' -v -p openstack/cinder

To print the contents of the last 30 reviews by 'John Smith'

    ./lastcomment.py -n 'John Smith'  -m

To specify a text file names.txt containing names to iterate through

    ./lastcomment.py -f names.txt

To print statistics on nova's third party CI accounts:

    ./lastcomment.py -p openstack/nova -c 60 -f nova.txt -v

To generate a html report for cinder's third party CI accounts on http://localhost:8000/report:

    ./lastcomment.py -p openstack/cinder -f cinder.txt -c 100 --json lastcomment.json
    python -m SimpleHTTPServer

Cloud-init
-----------

To run this on a cloud server using cloud-init use the ``user-data.txt`` file.
