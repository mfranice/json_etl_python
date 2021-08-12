import json
import requests
import matplotlib.pyplot as plt
from requests.api import request

url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

def fetch():

    response = requests.get(url)
    datos = response.json()
    resultados = datos["results"]

    dataset = [{'price':x.get('price'),'conditions':x.get('conditions')} for x in resultados if x['currency_id'] == 'ARS']

    print(dataset)

    return dataset


def transform(dataset, min, max):

    min_count = len([x for x in dataset if x['price'] < min])
    min_max_count = len([x for x in dataset if (min < x['price'] < max)])
    max_count = len([x for x in dataset if x['price'] > max])

    data = {'Cantidad menor al min': min_count, 'Cantidad entre min y max': min_max_count, 'Cantidad mayor al max': max_count}
    print(data)

    return data


def report(data):

    fig = plt.figure()
    fig.suptitle('Cantidad de depts. dentro y fuera del presupuesto', fontsize = 16)

    ax = fig.add_subplot()
    explode = (0, 0.2, 0)
    ax.pie(data.values(), labels = data.keys(), explode = explode, autopct='%1.1f%%', shadow = True)
    plt.show()
    

if __name__ == '__main__':

    dataset = fetch()
    min = int(input('Ingrese el valor mínimo del valor del alquiler que desea:\n'))
    max = int(input('Ingrese el valor máximo de alquiler que estaría dispuesto a pagar\n'))
    data = transform(dataset, min, max)
    report(data)

