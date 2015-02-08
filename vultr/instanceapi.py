#!/usr/bin/env python
#coding: utf-8

"""
A Python library to interact with Vultr's API.
Copyright (c) 2015 Levis Bakalinsky <levis.bakalinsky@fastmail.com>

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import requests
import json
import pprint

API_ENDPOINT = 'https://api.vultr.com'

class InstanceAPI():

	def __init__(self, api_key, api_version):
		self.api_endpoint = API_ENDPOINT
		self.api_key = api_key
		self.api_version = int(api_version)

		if self.api_version ==1:
			self.api_endpoint += '/v1'

	def snapshot_list(self):

		path = '/snapshot/list'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def snapshot_destroy(self, snapshot_id):

		path = '/snapshot/destroy'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SNAPSHOTID": snapshot_id, }
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def snapshot_create(self, sub_id, description):

		path = '/snapshot/create'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SUBID": sub_id, "description": description,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def iso_list(self):

		path = '/iso/list'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def plans_list(self):

		path = '/plans/list'
		url = self.api_endpoint + path
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def regions_list(self):

		path = '/regions/list'
		url = self.api_endpoint + path
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def regions_availability(self, dc_id):

		path = '/regions/availability'
		url = self.api_endpoint + path
		params = { "DCID": dc_id,}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def startupscript_list(self):

		path = '/startupscript/list'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def startupscript_destroy(self, script_id):

		path = '/startupscript/destroy'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SCRIPTID": script_id,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def sshkey_list(self):

		path = '/sshkey/list'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def sshkey_create(self, sshkey_name, sshkey_pub):

		path = '/sshkey/create'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "name": sshkey_name, "ssh_key": sshkey_pub, }
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def sshkey_update(self, sshkey_id, sshkey_name, sshkey_pub):

		path = '/sshkey/update'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key, "SSHKEYID": sshkey_id,}
		data = { "name": sshkey_name, "ssh_key": sshkey_pub, }
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def sshkey_destroy(self, sshkey_id):

		path = '/sshkey/destroy'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SSHKEYID": sshkey_id,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def server_list(self):

		path = '/server/list'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def server_bandwidth(self, sub_id):

		path = '/server/bandwidth'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key, "SUBID":sub_id,}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def server_reboot(self, sub_id):

		path = '/server/reboot'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SUBID": sub_id,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def server_halt(self, sub_id):

		path = '/server/halt'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SUBID": sub_id,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def server_destroy(self, sub_id):

		path = '/server/destroy'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SUBID": sub_id,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def server_reinstall(self, sub_id):

		path = '/server/reinstall'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SUBID": sub_id,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def server_restore_snapshot(self, sub_id, snapshot_id):

		path = '/server/restore_snapshot'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SUBID": sub_id, "SNAPSHOTID": snapshot_id,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def backup_list(self):

		path = '/backup/list'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def server_restore_backup(self, sub_id, backup_id):

		path = '/server/restore_backup'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SUBID": sub_id, "BACKUPID": backup_id,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

#######################################
# Need to handle optional parameters for create
# ipxe_chain_url
# ISOID
# SCRIPTID
# SNAPSHOTID
# enable_ipv6 
# enable_private_network
# label
# SSHKEYID
# auto_backups
#######################################

	def server_create(self, dc_id, vpsplan_id, os_id):  # Need to handle optional parameters (e.g startup scripts, use snapshot/backup, etc)

		path = '/server/create'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "DCID": dc_id, "VPSPLANID": vpsplan_id, "OSID": os_id,}
		method='POST'

		json = self.api_request(url, method, params, data )
		return json

#######################################
# Missing Endpoints
# /server/list_ipv4
# /server/reverse_set_ipv4
# /server/reverse_default_ipv4
# /server/list_ipv6
# /server/reverse_list_ipv6
# /server/reverse_set_ipv6
# /server/reverse_delete_ipv6
# /server/label_set
# /server/create_ipv4
# /server/destroy_ipv4
#######################################

	def server_oschange_list(self, sub_id):

		path = '/server/os_change_list'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key, "SUBID":sub_id,}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def server_oschange(self, sub_id, os_id):

		path = '/server/os_change'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key,}
		data = { "SUBID": sub_id, "OSID": os_id,}
		method='POST'

		json = self.api_request(url, method, params, data)
		return json

	def account_info(self):

		path = '/account/info'
		url = self.api_endpoint + path
		params = { "api_key": self.api_key}
		method='GET'

		json = self.api_request(url, method, params)
		return json

	def os_list(self):

		path = '/os/list'
		url = self.api_endpoint + path
		method='GET'

		json = self.api_request(url, method)
		return json

	def api_request(self, url, method, params={}):
		try:
			if method == 'GET':
				resp = requests.request(url=url, params=params, method=method)
				
			elif method == 'POST':
				resp = requests.request(url=url, params=params, data=data, method=method)
			else:
				print "method not supported!"

			if resp.status_code == 200:
				response = resp.json()
			else:
				response = str(resp.status_code) + ' - ' + resp.content

			return response

		except requests.exceptions.RequestException as e:
			print('HTTP Request failed')
 





