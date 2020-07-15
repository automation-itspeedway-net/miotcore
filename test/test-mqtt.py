# Test the MQTT module
# (c) Copyright Si Dunford, Jul 2020
#
# VERSION 1.1

import sys,time
from miot import mqtt

def on_error( broker, error ):
    try:
        err=str(error['id'])
        print( '# ERROR ('+err+'): '+error['message']+", "+broker.error( err ) )
    except Exception as e:
        print(e)

def on_connect( broker, msg ):
    print( "# Connect", str(msg ) )
    print( "- Broker=", broker.hostname )
    
    # Subscribe to topic
    result,mid = broker.subscribe( '#' )
    print( "- Subscribed with mid="+str(mid) )
    
    # Send message
    broker.publish( "miot/event", "test-mqtt.py connected" )

def on_disconnect( broker, msg ):
    print( "# Disconnect", broker.hostname, str(msg ) )

def on_publish( broker, msg ):
    print( "# Publish", broker.hostname, str(msg ) )

def on_subscribe( broker, msg ):
    print( "# Subscribe", broker.hostname, str(msg ) )

def on_unsubscribe( broker, msg ):
    print( "# Unsubscribe", broker.hostname, str(msg ) )

def on_message( broker, msg ):
    print( "# Message", broker.hostname, str(msg ) )
    pass

def main():
    #try:
    print( "* Create broker" )
    broker = mqtt.broker()
    #except Exception as e:
    #    print( e )
    #    sys.exit()

    print( "* Setup authentication" )
    broker.authenticate( 'RunForTheHills', 'AnotherFineMess' )

    # Add event handlers
    print( "* Setup event handlers" )
    broker.on( 'error', on_error )
    broker.on( 'connect', on_connect )
    broker.on( 'disconnect', on_disconnect )
    broker.on( 'publish', on_publish )
    broker.on( 'subscribe', on_subscribe )
    broker.on( 'unsubscribe', on_unsubscribe )
    broker.on( 'message', on_message )

    # Connect to broker
    print( "* Connecting to broker" )
    broker.connect( '192.168.1.228' )

    # AYNC Listener
    #broker.start()     # ASYNC
    # while running:
    #   do something
    # broker.stop()
    
    # SYNC Blocking
    broker.wait()       # SYNC (Blocking)

    # MANUAL Dispatch
    # while True:.
    #   broker.dispatch()
    
    #while True:
    # THIS IS BAD: SEE HERE
    # https://blog.miguelgrinberg.com/post/how-to-make-python-wait
    #    time.sleep(10)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

