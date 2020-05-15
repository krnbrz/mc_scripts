import sys
import urllib.request
import json

mojangManifestUrl = 'https://launchermeta.mojang.com/mc/game/version_manifest.json'

manifestRequest = urllib.request.urlopen(mojangManifestUrl)
manifestJson = json.loads(manifestRequest.read())

if len(sys.argv) > 1 and (sys.argv[1] == '-snapshot' or sys.argv[1] == '-s'):
    requestedVersion = manifestJson['latest']['snapshot']
else:
    requestedVersion = manifestJson['latest']['release']

releaseList = manifestJson['versions']

for release in releaseList:
    if release['id'] == requestedVersion:
        releaseUrl = release['url']
        break

releaseRequest = urllib.request.urlopen(releaseUrl)
releaseJson = json.loads(releaseRequest.read())
downloadUrl = releaseJson['downloads']['server']['url']

downloadRequest = urllib.request.urlopen(downloadUrl)

with open('server.jar', 'wb') as output:
    output.write(downloadRequest.read())

print ("Downloaded version: " + requestedVersion)
