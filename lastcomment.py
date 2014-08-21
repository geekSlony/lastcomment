"""Print the last time a reviewer(bot) left a comment."""

import json
import time

import requests


TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def main():
    # unique gerrit name of the reviewer
    #reviewer = "VMware NSX CI"
    reviewer = "Elastic Recheck"
    # Include review messages in query
    query = "https://review.openstack.org/changes/?q=reviewer:\"%s\"&o=MESSAGES" % (reviewer)
    r = requests.get(query)
    changes = json.loads(r.text[4:])
    last_date = None
    last_change_id = None
    for change in changes:
        date = last_comment(change, reviewer)
        if date > last_date:
            last_date = date
            last_change_id = change['change_id']
    print "last comment from '%s'" % reviewer
    print "timestamp: %s" % time.strftime(TIME_FORMAT, last_date)
    print "subject: '%s'" % change['subject']
    print "https://review.openstack.org/#q,%s,n,z" % last_change_id


def last_comment(change, name):
    """Return most recent timestamp for comment by name."""
    last_date = None
    for message in change['messages']:
        if 'author' in message and message['author']['name'] == name:
            date = message['date']
            # https://review.openstack.org/Documentation/rest-api.html#timestamp
            # drop nanoseconds
            date = date.split('.')[0]
            date = time.strptime(date, TIME_FORMAT)
            if date > last_date:
                last_date = date
    return last_date


if __name__ == "__main__":
    main()
