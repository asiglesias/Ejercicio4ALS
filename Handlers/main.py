#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def post(self):

        try:
            kilometros = float(self.request.get("kmInput", 0.0))
            tiempo = float(self.request.get("minutesInput", 0.0))
            consumo_medio = float(self.request.get("consumoInput", 0.0))
        except ValueError:
            self.response.write("<p>Alguno de los valores no era un numero</p>")
        velocidad_media = 0
        consumo_total = 0
        tiempoEnHoras = float(tiempo / 60)
        response = ""
        if tiempoEnHoras > 0:
            velocidad_media = kilometros / tiempoEnHoras
            response += "<p>La velocidad media es: {0} km/h</p>".format(velocidad_media)
        else:
            response += "<p>No se pudo calcular la velocidad media porque alguno de los parametros no era un numero o era igual a 0: <p>{0}</p> <p>{1}</p> </p>".format(type(kilometros), tiempo)


        response += "Consumo de {0} l/100km".format(kilometros * consumo_medio / 100)

        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/calcular', MainHandler)
], debug=True)
