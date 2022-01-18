from flask import Flask, request, render_template, url_for, redirect, json
from datetime import date
import os
app = Flask(__name__)

@app.route('/github', methods = ['POST', 'GETq'])
def github_hook():
	if request.method == 'POST':
		update_repo()
		return "completed"
	else:
		return ('wrong request')
		
def update_repo():
	today = date.today()
	
	os.system('cd /root/xrdocs/ncs5500/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('ncs5500 repo was updated')

	os.system('cd /root/xrdocs/ncs5500/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('ncs5500 repo was updated')

	os.system('cd /root/xrdocs/tdm2ip/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('tdm2ip repo was updated')

	os.system('cd /root/xrdocs/tdm2ip/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('tdm2ip repo was updated')

	os.system('cd /root/xrdocs/telemetry/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('telemetry repo was updated')

	os.system('cd /root/xrdocs/telemetry/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('telemetry repo was updated')

	os.system('cd /root/xrdocs/device-lifecycle/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('device-lifecycle repo was updated')

	os.system('cd /root/xrdocs/device-lifecycle/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('device-lifecycle repo was updated')

	os.system('cd /root/xrdocs/cloud-scale-networking/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('cloud-scale-networking repo was updated')

	os.system('cd /root/xrdocs/cloud-scale-networking/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('cloud-scale-networking repo was updated')

	os.system('cd /root/xrdocs/application-hosting/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('application-hosting repo was updated')

	os.system('cd /root/xrdocs/application-hosting/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('application-hosting repo was updated')

	os.system('cd /root/xrdocs/automation/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('automation repo was updated')

	os.system('cd /root/xrdocs/automation/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('automation repo was updated')

	os.system('cd /root/xrdocs/programmability/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('programmability repo was updated')

	os.system('cd /root/xrdocs/programmability/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('programmability repo was updated')

	os.system('cd /root/xrdocs/multicast/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('multicast repo was updated')

	os.system('cd /root/xrdocs/multicast/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('multicast repo was updated')

	os.system('cd /root/xrdocs/packet-fronthaul/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('packet-fronthaul repo was updated')

	os.system('cd /root/xrdocs/packet-fronthaul/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('packet-fronthaul repo was updated')

	os.system('cd /root/xrdocs/8000/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('8000 repo was updated')

	os.system('cd /root/xrdocs/8000/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('8000 repo was updated')

	os.system('cd /root/xrdocs/cnbng/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('8000 repo was updated')

	os.system('cd /root/xrdocs/cnbng/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('8000 repo was updated')

if __name__ == '__main__':
	app.run(host='64.225.112.234', port=7777, debug=True)