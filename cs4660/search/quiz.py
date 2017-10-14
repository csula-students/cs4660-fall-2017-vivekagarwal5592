"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response


def BFS ( initial_node, dest_node):
    Q = []
    visited_nodes = []
    parent = {}
    nodes_distance = {}
    Q.append(initial_node['id'])
    parent[initial_node['id']] = None
    nodes_distance[initial_node['id']] = 0
    last_node = dest_node['id']
    visited_nodes.append(initial_node['id'])
    while (bool(Q)):
        current_node = Q.pop(0)
        neighbors =  get_state(initial_node['id'])
        print(neighbors)
        for neighbor in neighbors.items():
            if (neighbor not in visited_nodes):
                Q.append(neighbor)
                graph_distance = get_Euclidean_distance(current_node, neighbor)
                nodes_distance[neighbor] = nodes_distance[current_node] + graph_distance
                parent[neighbor] = current_node
                visited_nodes.append(neighbor['id'])
        if (last_node in visited_nodes):
            break



    list = []
    while parent[last_node] is not None:
        print (last_node)
        last_node = parent[last_node]

    return list


def Dijakstras():
    pass


def get_Euclidean_distance(a,b):
    node1 =  get_state(a)
    node2 = get_state(b)
    xdifference = ((node1['location']['x'] - node2['location']['x']) ** 2)
    ydifference =  ((node1['location']['y'] - node2['location']['y']) ** 2)
    dis = ((xdifference + ydifference)**0.5)
    return dis


if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    #print("empty")
    #print(empty_room['neighbors'])
    BFS(empty_room, empty_room['neighbors'][0])
   # Dijakstras(empty_room, empty_room['neighbors'][0])

#print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))







