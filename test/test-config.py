# Test the config module
# (c) Copyright Si Dunford, Jul 2020
#
# VERSION 1.1

from miot import config

print( config.tostring() )

# TEST CONFIG
print( "RESULT="+config.get( "mqtt.host", "xyz" ) )
print( "RESULT="+config.get( "mqtt.default.host", "abc" ) )
print( "RESULT="+config.get( "rss.feed", "123" ) )

print( config.tostring() )

config.wipe()
config.default()

config.set( "mqtt.host", "192.168.1.228" )
config.set( "mqtt.default.host", "192.168.1.253" )
config.set( "rss.itspeedway", {'url':"https://itspeedway.net"} )
config.set( "rss.bbc", {'url':"https://bbc.co.uk"} )

config.save()

print( config.tostring() )


