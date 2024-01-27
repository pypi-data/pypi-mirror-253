###Documentación en https://github.com/lucasbaldezzari/sarapy/blob/main/docs/Docs.md

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import warnings
from sarapy.dataProcessing import TLMSensorDataExtractor, TimeSeriesProcessor, GeoProcessor

class FMCreator(BaseEstimator, TransformerMixin):
    """La clase FMCreator se encarga de crear la Feature Matrix (FM) a partir de los datos de telemetría. Se utilizan las clases TLMSensorDataExtractor, TimeSeriesProcessor y GeoProcessor para realizar las transformaciones necesarias.
    
    Versión 0.1.0
    
    En esta versión la matriz de características está formada por las siguientes variables
    
    - DST_PT: Distorsión de plantín
    - DST_FT: Distorsión de fertilizante
    - deltaO: delta operación
    - ratio_dCdP: Ratio entre el delta de caminata y delta de pico abierto
    - distances: Distancias entre operaciones
    """
    
    def __init__(self):
        """Inicializa la clase FMCreator."""
        
        self.is_fitted = False
        
    def fit(self, X: np.array, y=None)-> np.array:
        """Fittea el objeto
        
        Params:
            - X: Es un array con los datos provenientes (strings) de la base de datos histórica. La forma de X es (n,4)Las columnas de X son,
                - 0: tlm_spbb son los datos de telemetría.
                - 1: date_oprc son los datos de fecha y hora de operación.
                - 2: latitud de la operación
                - 3: longitud de la operación
        """
        
        ##agregar asserts y warnings
        
        tlm_spbb = X[0] #datos de telemería
        date_oprc = X[1].astype(int) #datos de fecha y hora de operación
        lats = X[2].astype(float) #latitudes de las operaciones
        longs = X[3].astype(float) #longitudes de las operaciones        
        
        ##instanciamos los objetos
        tlmDataExtractor = TLMSensorDataExtractor()
        timeProcessor = TimeSeriesProcessor()
        geoprocessor = GeoProcessor()
        
        ##fitteamos tlmse con los datos de telemetría
        self._tlmExtracted = tlmDataExtractor.fit_transform(tlm_spbb)
        
        ##fitteamos timeProcessor con los datos de fecha y hora de operación y los TIMEAC
        timeData = np.hstack((date_oprc.reshape(-1,1),self._tlmExtracted[:,7].reshape(-1, 1)))
        self._timeDeltas = timeProcessor.fit_transform(timeData)
        
        ##fitteamos geoprocessor con las latitudes y longitudes
        ##genero un array de puntos de la forma (n,2)
        points = np.hstack((lats.reshape(-1,1),longs.reshape(-1,1)))
        self._distances = geoprocessor.fit_transform(points)
        
        self.is_fitted = True
        
    def transform(self, X: np.array, y = None):
        """Transforma los datos de X en la matriz de características.
        
        Params:
            - X: Es un array con los datos provenientes (strings) de la base de datos histórica. La forma de X es (n,4)Las columnas de X son,
                - 0: tlm_spbb son los datos de telemetría.
                - 1: date_oprc son los datos de fecha y hora de operación.
                - 2: latitud de la operación
                - 3: longitud de la operación
                
        Returns:
            - featureMatrix: Es un array con la matriz de características. La forma de featureMatrix es (n,5). Las columnas de featureMatrix son,
                - 0: DST_PT: Distorsión de plantín
                - 1: DST_FT: Distorsión de fertilizante
                - 2: deltaO: delta operación
                - 3: ratio_dCdP: Ratio entre el delta de caminata y delta de pico abierto
                - 4: distances: Distancias entre operaciones
        """
        
        if not self.is_fitted:
            raise RuntimeError("El modelo no ha sido fitteado.")
        
        ##creamos un diccionario para saber la posición de cada dato dentro del array devuelto por transform()
        self._dataPositions = {
            0: "DST_PT", 1: "DST_FT",
            2: "deltaO", 3: "ratio_dCdP", 4: "distances"}
        
        ##armamos la feature matrix
        featureMatrix = np.vstack((self._tlmExtracted[:,9],
                                   self._tlmExtracted[:,12],
                                   self._timeDeltas[:,0],
                                   self._timeDeltas[:,3],
                                   self._distances)).T
        
        return featureMatrix

    def fit_transform(self, X: np.array, y=None):
        """Fittea y transforma los datos de X en la matriz de características.
        
        Params:
            - X: Es un array con los datos provenientes (strings) de la base de datos histórica. La forma de X es (n,4)Las columnas de X son,
                - 0: tlm_spbb son los datos de telemetría.
                - 1: date_oprc son los datos de fecha y hora de operación.
                - 2: latitud de la operación
                - 3: longitud de la operación
        
        Returns:
            - featureMatrix: Es un array con la matriz de características. La forma de featureMatrix es (n,5). Las columnas de featureMatrix son,
                - 0: DST_PT: Distorsión de plantín
                - 1: DST_FT: Distorsión de fertilizante
                - 2: deltaO: delta operación
                - 3: ratio_dCdP: Ratio entre el delta de caminata y delta de pico abierto
                - 4: distances: Distancias entre operaciones
        """
        self.fit(X)
        return self.transform(X)
    
    @property
    def tlmExtracted(self):
        """Devuelve los datos de telemetría extraídos."""
        return self._tlmExtracted
    
    @property
    def timeDeltas(self):
        """Devuelve los datos de tiempo extraídos."""
        return self._timeDeltas
    
    @property
    def distances(self):
        """Devuelve las distancias entre operaciones."""
        return self._distances
    
        
if __name__ == "__main__":
    ##genero objeto FMCreator
    fmcreator = FMCreator()
    
    ##datos de ejemplo
    tlmsbp_sample = np.array(['0010001000010010110000011000000111111101001000000000000000000000',
                              '0010001000010100110000011000000111111101001000000000000000000000',
                              '0010001000010000110000011000000111111101001000000000000000000000',
                              '0010001000011010110000011000110111111101001000000000000000000000'])
    
    date_oprc = np.array(["35235", "35240", "35244", "35248"])
    lats = ["-32.331093", "-32.331116", "-32.331131", "-32.331146"]
    lons = ["-57.229733", "-57.229733", "-57.229733", "-57.22974"]
    
    ##generamos matriz de datos X
    X = np.array([tlmsbp_sample, date_oprc, lats, lons])
    fmcreator.fit(X)
    fm = fmcreator.fit_transform(X)
    print(fm)