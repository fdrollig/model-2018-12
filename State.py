class State:
    FONTSIZE = "8"
    def __init__(self):
        self.locations = []
        self.step = 0
        self.comment = ""
    def calculateAmount(self, sympyExpr, params):
        return sympyExpr.evalf(4, subs=params.valuesByNames)
        
    def draw(self, params):
        if (len(params.name) > 0):
            title = "Scenario: " + params.name + "\\n"
        else:
            title = ""
        if (len(self.comment) > 0):
            graphLabel = title + "Step " + str(self.step) + ": " + self.comment
        else:
            graphLabel = title + "Step " + str(self.step)
        
        graph = Digraph(node_attr={'fontname': 'Liberation Mono',
                                  'fontsize': State.FONTSIZE}, 
                       graph_attr={'fontname': 'Liberation Mono',
                                   'label': graphLabel,
                                  'fontsize': State.FONTSIZE}
                       )
        i = 1
        objNr = 1
        for loc in self.locations:
            subGraphId = "cluster"+str(i)
            subGraph = Digraph(name=subGraphId, node_attr={'shape': 'box'}, 
                               graph_attr={'fontname': 'Liberation Mono',
                                           'label': loc.name,
                                          'fontsize': State.FONTSIZE})
            for obj in loc.objects:
                if (isinstance(obj, Resource)):
                    amountTxt = ""
                    if (len(obj.amounts) > 0):
                        for amount in obj.amounts:
                            if (len(amountTxt) > 0):
                                amountTxt += "\\n"
                            amountTxt += amount.name
                            amountTxt += " =\\n= "
                            amountTxt += str(amount.quantity)
                            # Insert here a numeric value of the expression
                            numericAmount = self.calculateAmount(amount.quantity, params)
                            amountTxt += "\\n= "
                            amountTxt += str(numericAmount)
                            amountTxt += " ["
                            amountTxt += amount.unit
                            amountTxt += "]"
                        amountTxt = "\\n" + amountTxt
                subGraph.node("obj" + str(objNr), obj.name+amountTxt)
                objNr = objNr + 1
            
            if (len(loc.objects) == 0):
                subGraph.node("obj" + str(objNr), "", shape="none")
                objNr = objNr + 1
                
            graph.subgraph(subGraph)
            i = i + 1
        return graph
    
    def printInventory(self, txs):
        display(HTML("<h3>Inventory</h3>"))
        inventoryTable = ""
        inventoryTable += "<table>"
        inventoryTable += "<tr>"
        inventoryTable += "<th>Resource</th>"
        inventoryTable += "<th>Unit</th>"
        inventoryTable += "<th>Amount</th>"
        inventoryTable += "<th>Transaction</th>"
        inventoryTable += "<th>Step</th>"
        inventoryTable += "</tr>"
        for invTx in txs:
            inventoryTable += "<tr>"
            inventoryTable += "<td>"
            inventoryTable += invTx.resource
            inventoryTable += "</td>"
            inventoryTable += "<td>"
            inventoryTable += invTx.unit
            inventoryTable += "</td>"
            inventoryTable += "<th>"
            inventoryTable += str(invTx.amount)
            inventoryTable += "</td>"
            inventoryTable += "<td>"
            inventoryTable += invTx.comment
            inventoryTable += "</td>"
            inventoryTable += "<td>"
            inventoryTable += str(invTx.simStep)
            inventoryTable += "</td>"
            inventoryTable += "</tr>"                
        inventoryTable += "</table>"
        display(HTML(inventoryTable))
    
    def acctView(self):
        # Find all accounts in all locations which have more than 0 txs
        # and store them in acctsToDisplay
        acctsToDisplay = []
        for loc in self.locations:
            for curAcct in loc.accounts:
                if (curAcct):
                    acctsToDisplay.append((loc, curAcct))
        acctsToDisplay.sort(key=lambda tup: tup[0])
        lastLocName = ""
        lastLoc = None
        for locAcctTuple in acctsToDisplay:
            loc = locAcctTuple[0]
            acct = locAcctTuple[1]
            if lastLoc == None:
                lastLocName = loc.name
                lastLoc = loc
                display(HTML("<h2>" + loc.name + "</h2>"))
            elif (lastLocName != loc.name):
                self.printInventory(lastLoc.inventory.txs)
                display(HTML("<h2>" + loc.name + "</h2>"))
                lastLocName = loc.name
                lastLoc = loc
            display(HTML("<h3>" + acct.name + " @ " + loc.name + "</h3>"))
            tableHtml = "<table border=1><tr><th>Credit</th><th>Debit</th><th>Transaction</th><th>Step</th></tr>"            
            for creditTx in acct.creditTxs:
                tableHtml += "<tr>"
                tableHtml += "<td>" # Credit
                tableHtml += str(creditTx.amount)
                tableHtml += "</td>"
                tableHtml += "<td>" # Debit
                tableHtml += "</td>"
                tableHtml += "<td>" # Transaction
                tableHtml += creditTx.comment
                tableHtml += "</td>"
                tableHtml += "<td>" # Step
                tableHtml += str(creditTx.simStep)
                tableHtml += "</td>" # Step
                tableHtml += "</tr>"
            for debitTx in acct.debitTxs:
                tableHtml += "<tr>"
                tableHtml += "<td>" # Credit
                tableHtml += "</td>"
                tableHtml += "<td>" # Debit
                tableHtml += str(debitTx.amount)
                tableHtml += "</td>"
                tableHtml += "<td>" # Transaction
                tableHtml += debitTx.comment
                tableHtml += "</td>"
                tableHtml += "<td>" # Step
                tableHtml += str(debitTx.simStep)
                tableHtml += "</td>" # Step
                tableHtml += "</tr>"
            tableHtml += "</table>"
            display(HTML(tableHtml))

