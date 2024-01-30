from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
import numpy as np

class index:
    def __init__(self):
        pass

    def build_index(self, E):
        """Builds an index for each element of E
        E[i] should return the i-th element"""
        try:
            self.elements = np.unique(E, axis=0)
        except:
            #Si les elements de E ne sont pas homogene en dim np.unique ne fonctionne pas 
            self.elements = []
            for e in E:
                add = True
                for elt in self.elements:
                    if str(elt) == str(e):
                        add = False
                if add:
                    self.elements += [e]


        self.idx = {}
        for ei, e in enumerate(self.elements):
            self.idx[str(e)] = ei

    def __call__(self, x):
        """Fonction de E dans [|0,#E-1|] qui index E"""
        out = np.zeros(len(x))
        for xi, xx in enumerate(x):
            out[xi] = self.idx[str(xx)]
        return out.astype(int)

    def inv(self, n):
        """Fonction de [|0,#E-1|] qui associe a chaque index son element de E"""
        try:
            return self.elements[n]
        except:
            return [self.elements[n[i]] for i in range(len(n))]

class indexFunction:
    def __init__(self):
        pass

    def build_index(self, phi, psi):
        """Associe a chaque classifieur sur le indexes, un classifieur sur les elemens."""
        self.phi = phi
        self.psi = psi

    def __call__(self, f, n):
        """Fonction sur les elements a passer sur les indexes"""
        return self.psi(f(self.phi.inv(n)))

    def inv(self, g, e):
        """Fonction sur les indexes a passer sur les elements"""
        return self.psi.inv(g(self.phi(e)))


class optimalBA:
    def __init__(self):
        pass

    def fit(self,x,y):
        xcat = np.unique(x)
        ycat = np.unique(y)
        m = len(xcat)
        n = len(ycat)
        e = np.zeros([m,n]).astype(float)
        for j in range(n):
            ymask = y==j
            s = np.sum(ymask)
            for i in range(m):
                e[i,j] = np.sum((x==i)&ymask)/s

        self.f = np.argmax(e,axis=1) #Merci ♥
        self.e = e

    def predict(self,x):
        return self.f[x]

    def predict_proba(self, x):
        #TODO
        pass

class FinitClassifier:
    def __init__(self, unseen=False):
        """unseen (bool): Vrai si on compte evaluer sur des données non-vues à l'entrainement."""
        self.phi = index()
        self.psi = index()
        self.Phi = indexFunction()
        self.model = optimalBA()
        self.unseen = unseen

    def fit(self,y,z):
        self.scaler = StandardScaler()
        self.scaler.fit(y)
        yscal = self.scaler.transform(y)
        self.phi.build_index(yscal)
        self.psi.build_index(z)
        self.Phi.build_index(self.phi,self.psi)
        yidx = self.phi(yscal)
        zidx = self.psi(z)
        self.model.fit(yidx, zidx)

    def is_seen(self,y):
        yscal = self.scaler.transform(y)
        mask = np.zeros(np.shape(yscal)[0]).astype(bool)
        for xi,x in enumerate(yscal):
            mask[xi] = str(x) in self.phi.idx.keys()
        return mask
             
    def predict(self, y):
        yscal = self.scaler.transform(y)
        if self.unseen:
            #Si on evalu sur des données non-vues à l'entraînement 
            #MAJ de l'index phi
            for x in yscal:
                if not(str(x) in self.phi.idx.keys()):
                    dist = []
                    for xx in self.phi.elements:
                        dist += [np.mean(np.linalg.norm(x-xx))]
                    near = self.phi.elements[np.argmin(dist)]
                    self.phi.idx[str(x)] = self.phi.idx[str(near)]
        return self.Phi.inv(self.model.predict, yscal)
