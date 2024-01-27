import time
import pyjs8call
import random

def inbox(msgs):
    for msg in msgs:
        print('\tinbox: {0}'.format(msg['text']))

def tx(msg):
    print('\tid: {0}\tstatus: {1}'.format(msg.id, msg.status))

def spots(msgs):
    for msg in msgs:
        print('\tspot: {0}'.format(msg.origin))

def spot_station(msg):
    print('\tspot station: {0}'.format(msg.origin))

def spot_group(msg):
    print('\tspot group: {0}'.format(msg.destination))

def generate_spots():
    global js8call
    msgs = []

    for i in range(50):
        msg = pyjs8call.Message()
        msg.type = pyjs8call.Message.RX_DIRECTED
        msg.grid = random.choice(['E', 'F', 'G']) + random.choice(['M', 'N', 'O', 'P']) + str(random.randrange(0, 9)) + str(random.randrange(0, 9))
        distance, bearing = js8call.grid_distance(msg.grid)
        msg.distance = distance
        msg.bearing = bearing
        msg.timestamp -= random.randrange(10, 60*60*3)
        msg.origin = random.choice(['KC3KVT', 'KC3WPA', 'KC3WNC', 'KC3TFL'])
        msg.destination = random.choice(['KC5KVT', '@HB', 'KC3KVT'])
        msgs.append(msg)

    return msgs

js8call = pyjs8call.Client()
#js8call.callback.inbox = inbox
#js8call.callback.outgoing = tx
#js8call.callback.spots = spots
#js8call.callback.station_spot = spot_station
#js8call.callback.group_spot = spot_group
js8call.settings.set_speed('fast')
js8call.start()
#js8call.inbox_monitor.enable(interval=3)
#js8call.spot_monitor.add_station_watch('KC3KVT')
#js8call.spot_monitor.add_group_watch('@HB')
#js8call.offset.pause_monitoring()
#js8call.heartbeat.enable_networking(interval=3)
#time.sleep(1)
#js8call.js8call._spots = generate_spots()


