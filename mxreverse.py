#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dns.resolver
import dns.reversename
import json
import urlparse


def resolve_mx(hostname):
    response = []
    for data in dns.resolver.query(hostname, 'MX'):
        response.append((data.exchange.to_text(), data.preference))
    return response


def resolve_ip(hostname):
    response = []
    for data in dns.resolver.query(hostname, 'A'):
        response.append(data.address)
    return response


def resolve_ptr(ip):
    try:
        for data in dns.resolver.query(dns.reversename.from_address(ip), 'PTR'):
            return data.target.to_text()
    except dns.resolver.NXDOMAIN:
        pass
    return ''


def check_mx(domainname):
    mails = resolve_mx(domainname)
    in_all = True
    in_any = False
    response = []
    for mx in mails:
        ips = []
        for ip in resolve_ip(mx[0]):
            ptr = resolve_ptr(ip)
            host_in = ptr == mx[0]
            if host_in:
                in_any = True
            else:
                in_all = False
            ips.append({'ip': ip, 'ptr': ptr, 'check': host_in})
        response.append({'name': mx[0], 'preference': mx[1], 'ips': ips})
    return {'domain': domainname, 'mx': response, 'all': in_all, 'any': in_any}


def application(environ, start_response):
    query = urlparse.parse_qs(environ.get('QUERY_STRING', ''))
    status = '200 OK'
    response_headers = [('Content-type', 'application/json')]
    try:
        content = check_mx(query['domain'][0])
    except Exception as e:
        status = '400 ERROR'
        content = {'message': e.message}
    start_response(status, response_headers)
    return [json.dumps(content).encode('utf-8')]
