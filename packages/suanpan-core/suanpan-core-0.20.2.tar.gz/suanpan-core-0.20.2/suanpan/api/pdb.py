from suanpan.api.requests import affinity


def listGraphs():
    return affinity.post("/pdb/api/v1/graph/list")["data"]


def getGraph(graphId):
    return affinity.post("/pdb/api/v1/graph/get", json={'graphId': graphId})["data"]


def getGraphTypes(graphId):
    return affinity.post("/pdb/api/v1/graph/type", json={'graphId': graphId})["data"]


def getGraphRelations(graphId):
    return affinity.post("/pdb/api/v1/graph/relation", json={'graphId': graphId})["data"]


def getObject(graphId, uid: str):
    return affinity.post("/pdb/api/v1/object/get", json={'graphId': graphId, 'uid': uid})["data"]


def getObjectChildren(graphId, uid: str):
    return affinity.post("/pdb/api/v1/object/children", json={'graphId': graphId, 'uid': uid})["data"]


def _getIndex(graphId, parentUid: str):
    index = 0
    children = getObjectChildren(graphId, parentUid)
    for child in children:
        for c in child["x.parent"]:
            if c["uid"] == parentUid:
                i = c["x.parent|x.index"]
                if i > index:
                    index = i

    return index + 1


def addObject(graphId, data):
    if isinstance(data, list):
        objs = data
    else:
        objs = [data]
    for obj in objs:
        parents = obj["x.parent"]
        for parent in parents:
            parent["x.parent|x.index"] = _getIndex(graphId, parent["uid"])

    return affinity.post("/pdb/api/v1/object/add", json={'graphId': graphId, 'set': objs})["data"]


def updateObject(graphId, update=None, delete=None):
    data = {'graphId': graphId}
    if update:
        if isinstance(update, list):
            data['set'] = update
        else:
            data['set'] = [update]

    if delete:
        if isinstance(delete, list):
            data['delete'] = delete
        else:
            data['delete'] = [delete]

    return affinity.post("/pdb/api/v1/object/update", json=data)["data"]


def deleteObject(graphId, uid: str):
    return affinity.post("/pdb/api/v1/object/delete", json={'graphId': graphId, 'uid': uid})


def addObjectRelation(graphId, relationId: str, srcUid: str, dstUids: list):
    return affinity.post("/pdb/api/v1/object/relation/add", json={
        'graphId': graphId,
        'set': [{'uid': srcUid, relationId: dstUids}]
    })["data"]


def deleteObjectRelation(graphId, relationId: str, srcUid: str, dstUids: list):
    return affinity.post("/pdb/api/v1/object/relation/delete", json={
        'graphId': graphId,
        'delete': [{'uid': srcUid, relationId: dstUids}]
    })["data"]


def searchObjectWithType(graphId, types, attrs=None, constraints=None):
    data = {'graphId': graphId, 'type': types}
    if attrs:
        data['attrs'] = attrs
    if constraints:
        data['constraints'] = constraints

    return affinity.post("/pdb/api/v1/object/search/type", json=data)["data"]
