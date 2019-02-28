class StateTransition:
    def run(self, oldState):
        return copy.deepcopy(oldState)
    def findByName(self, lst, name):
        iterator = filter(lambda elem: elem.name == name, lst)
        return next(iterator)
    def removeFromLoc(self, state, locName, resourceName):
        loc = self.findByName(state.locations, locName)
        resource = self.findByName(loc.objects, resourceName)
        loc.objects.remove(resource)
    
    def move(self, state, resourceName, srcLoc, targetLoc):
        src = self.findByName(state.locations, srcLoc)
        target = self.findByName(state.locations, targetLoc)
        resource = self.findByName(src.objects, resourceName)
        src.objects.remove(resource)
        target.objects.append(resource)
    def put(self, state, resourceName, targetLoc):
        target = self.findByName(state.locations, targetLoc)
        resource = Resource(resourceName)
        target.objects.append(resource)
    def findAccount(self, state, locName, accountName):
        loc = self.findByName(state.locations, locName)
        iterator = filter(lambda elem: elem.name == accountName, loc.accounts)
        return next(iterator)
    def acctTx(self, tx, cAcct, dAcct):
        cAcct.enterCredit(tx)
        dAcct.enterDebit(tx)
