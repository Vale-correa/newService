#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install Flask


# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import abort
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
clientes = [{
    'id':'45483228',
    'name':'patricia barcos',
    'direccion':'los alpes',
    'postal':'12345'
}]
paqueteB=[{'idpaquet':'1234',
          'namepaquet':'carro',
          'preciopaquet':'3500',
          'destino':'londres',
          }]
factura=[]

@app.route('/clients/',methods=['GET'])
def get_allclients():
    return jsonify({'clients': clientes})

@app.route('/clients/<stdId>',methods=['GET'])
def get_clients(stdId):
    usr = [std for std in clientes if (std['id'] == stdId)]
    return jsonify({'est': usr})

@app.route('/clients/<stdId>',methods=['PUT'])
def update_clients(stdId):
    row = [est for est in clientes if (est['id'] == stdId)]
    if 'name' in request.json:
        row[0]['name'] = request.json['name']
    if 'direccion' in request.json:
        row[0]['direccion'] = request.json['direccion']
    if 'postal' in request.json:
        row[0]['postal'] = request.json['postal']
    return jsonify({'est': row[0]})

@app.route('/clients/',methods=['POST'])
def create_clients():
    dat = {
    'id': request.json['id'],
    'name': request.json['name'],
    'direccion': request.json['direccion'],
    'postal': request.json['postal']    
    }
    clientes.append(dat)
    return jsonify(dat)

@app.route('/clients/<stdId>',methods=['DELETE'])
def deleteEmp(stdId):
    row = [est for est in clients if (est['id'] == stdId)]
    if len(row) == 0:
       abort(404)
    clientes.remove(row[0])
    return jsonify({'response': 'Success'})


@app.route('/paquetes/',methods=['GET'])
def get_allpaquetes():
    return jsonify({'paquetes': paqueteB})

@app.route('/paquetes/<pqtId>',methods=['GET'])
def get_paquetes(pqtId):
    paq = [pqt for pqt in paqueteB if (pqt['idpaquet'] == pqtId)]
    return jsonify({'pqt': paq})

@app.route('/paquetes/<pqtId>',methods=['PUT'])
def update_paquetes(pqtId):
    row = [pqt for pqt in paqueteB if (pqt['idpaquet'] == pqtId)]
    if 'namepaquet' in request.json:
        row[0]['namepaquet'] = request.json['namepaquet']
    if 'preciopaquet' in request.json:
        row[0]['preciopaquet'] = request.json['preciopaquet']
    if 'destino' in request.json:
        row[0]['destino'] = request.json['destino']
    return jsonify({'pqt': row[0]})


@app.route('/paquetes/',methods=['POST'])
def create_paquetes():
    dat = {
    'idpaquet': request.json['idpaquet'],
    'namepaquet': request.json['namepaquet'],
    'preciopaquet': request.json['preciopaquet'],
    'destino': request.json['destino'],
    'trayectoria': request.json['trayectoria']
    }
    paqueteB.append(dat)
    return jsonify(dat)

@app.route('/paquetes/trayectoria/<destino>',methods=['GET'])
def trayecto(destino):
    trayectoriaB = {
        'local': 3500,
        'Centro America': 5000,
        'Norte America': 7500,
        'Sur America': 7200,
        'Europa': 12000,
        'Asia': 13500,
        'Africa': 11350
    }
    return jsonify(trayectoriaB[destino])

@app.route('/Factura/',methods=['POST'])
def create_factura():
    fact = {
    'idfactura': request.json['idfactura'],
    'nameclient': request.json['nameclient'],
    'paquetes': request.json['paquetes'],
    'total': request.json['total']
    }
    clientes.append(fact)
    return jsonify(fact)

@app.route('/factura/<idfactura>', methods=['GET'])
def getfact(idfactura):
    fact=[qwe for qwe in factura if (qwe['idfactura']==idfactura)]
    
    return jsonify({qwe:fact})


if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




