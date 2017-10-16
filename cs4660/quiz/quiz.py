"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""
from graph import graph as g
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


def BFS (initial_room, dest_room):
    print('BFS')
    from_Node = g.Node( get_state(initial_room))
    to_Node = g.Node( get_state(dest_room))
    Obj = g.ObjectOriented()
    Obj.add_node(from_Node)
    Obj.add_node(to_Node)
    Q = []
    visited_nodes = []
    parent = {}
    nodes_distance = {}
    Q.append(from_Node)
    parent[from_Node.data['id']] = None
    nodes_distance[from_Node.data['id']] = 0
    last_node = to_Node
    visited_nodes.append(from_Node.data['id'])
    while (bool(Q)):
        current_node = Q.pop(0)
        for neighbor in  (current_node.data['neighbors']):
            if (neighbor['id'] not in visited_nodes):
                Q.append(g.Node(get_state(neighbor['id'])))
                parent[neighbor['id']] = current_node
                visited_nodes.append(neighbor['id'])
        if (last_node.data['id'] in visited_nodes):
            break

    list = []
    while parent[last_node.data['id']] is not None:
        a = transition_state(parent[last_node.data['id']].data['id'],last_node.data['id'])
        print (str(parent[last_node.data['id']].data['id'])+','+str(last_node.data['id'])+':'+str(a['event']['effect']))
        last_node = parent[last_node.data['id']]
    return list


def Dijakstras(initial_room, dest_room):
    print('Dijakstras')
    Obj = g.ObjectOriented()
    grey_nodes = []
    Q = {}
    visited_nodes = []
    parent = {}
    nodes_distance = {}
    Q[initial_room] = 0
    parent[initial_room] = None
    nodes_distance[initial_room] = 0
    last_node = dest_room
    visited_nodes.append(initial_room)
    while (bool(Q)):
        current_node = max(Q, key=Q.get)
        Q.pop(current_node)
        visited_nodes.append(current_node)
        Obj.add_node(g.Node(current_node))
        a = get_state(current_node)
        q = a['neighbors']
        for i in q:
            Obj.add_node(g.Node(i['id']))
            a = transition_state(a['id'], i['id'])
            Obj.add_edge(g.Edge(g.Node(current_node),g.Node(i['id']),a['event']['effect']))
        for neighbor in q:
            if ((neighbor['id'] not in visited_nodes and neighbor['id'] not in grey_nodes)):
                Q[neighbor['id']]= nodes_distance[current_node] + Obj.distance(g.Node(current_node),g.Node(neighbor['id']))
                (nodes_distance[neighbor['id']]) = nodes_distance[current_node] +Obj.distance(g.Node(current_node),g.Node(neighbor['id']))
                parent[neighbor['id']] = current_node
                grey_nodes.append(neighbor['id'])

        if (last_node in visited_nodes):
            break
    list = []
    while parent[last_node] is not None:
        a = transition_state(parent[last_node], last_node)
        print(str(parent[last_node]) +','+ str(last_node)+':'+str(a['event']['effect']))
        list = [last_node] + list
        last_node = parent[last_node]
    return list


if __name__ == "__main__":
    empty_room = '7f3dc077574c013d98b2de8f735058b4'
    destination_room = 'f1f131f647621a4be7c71292e79613f9'
    BFS(empty_room,destination_room)
    Dijakstras(empty_room,destination_room)








