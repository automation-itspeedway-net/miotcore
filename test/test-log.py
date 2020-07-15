# Test the log module
# (c) Copyright Si Dunford, Jul 2020
#
# VERSION 1.1

from miot import log

# OPTIONAL : Set the log file format
#log.format()
#log.format( log.SYSLOG )
log.format( log.DAEMON )

log.debug( "Test DEBUG Message" )
log.info( "Test INFO Message" )
log.notice( "Test NOTICE Message" )
log.warning( "Test WARNING Message" )
log.error( "Test ERROR Message" )
log.critical( "Test CRITICAL Message" )
log.alert( "Test ALERT Message" )
log.emergency( "Test EMERGENCY Message" )

# Force an exception
try:
    x = 1 / 0
except ZeroDivisionError as e:
    log.exception( 'ZeroDivisionError: %s', e )



